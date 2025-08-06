# command.py

import argparse
import shutil
import subprocess
import sys
import json
import zipfile
import tempfile
import urllib.request
import urllib.parse
from pathlib import Path
from cptd_tools.os_guard import is_compatible, _load_manifest
import cptd_tools.commands
import platform  
from cptd_tools.syntax_utils import print_help

try:
    import yaml
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml"], check=True)
    import yaml

SYNTAX = {
    "name": "command",
    "description": "Add or delete CLI command folders into the CPTD DSL system",
    "usage": "cptd command --add <file.zip> [--with-deps] | --del <command_name>",
    "arguments": [
        {"name": "--add", "required": False, "help": "ZIP archive of the command folder to add"},
        {"name": "--with-deps", "required": False, "help": "Automatically install dependencies from manifest"},
        {"name": "--del", "required": False, "help": "Command folder name to delete"},
        {"name": "--allow-insecure", "required": False, "help": "Allow commands with dangerous code (e.g. pip install). Not recommended."}

    ],
    "examples": [
        "cptd command --add mycommand.zip --with-deps",
        "cptd command --del mycommand",
        "cptd command --add https://yourdomain.com/plugins/mycommand.zip --with-deps"
        ]
}

def load_manifest(manifest_path: Path) -> dict:
    if manifest_path.suffix == '.yaml':
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    elif manifest_path.suffix == '.json':
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported manifest format: {manifest_path.name}")

def contains_forbidden_code(dir_path: Path, allow_insecure: bool = False) -> bool:
    for py_file in dir_path.rglob("*.py"):
        content = py_file.read_text(encoding='utf-8')
        if 'pip install' in content or ('subprocess' in content and 'install' in content):
            if allow_insecure:
                print(f"[⚠] Insecure code allowed by user in {py_file}. Proceeding anyway.")
                continue
            print(f"[⛔] Forbidden code in {py_file}: auto-install is not allowed.")
            return True
    return False


def install_dependencies_from_manifest(manifest_file: Path, auto_confirm: bool = False):
    try:
        manifest = load_manifest(manifest_file)
        deps = manifest.get("dependencies", [])
        if deps:
            print(f"[•] Dependencies listed: {', '.join(deps)}")
            if auto_confirm:
                subprocess.run([sys.executable, "-m", "pip", "install", *deps], check=True)
                print("[✓] Dependencies installed.")
            else:
                answer = input("[?] Install dependencies via pip? [Y/n]: ").strip().lower()
                if answer in ("", "y", "yes"):
                    subprocess.run([sys.executable, "-m", "pip", "install", *deps], check=True)
                    print("[✓] Dependencies installed.")
                else:
                    print("[!] Skipped installing dependencies.")
        else:
            print("[ℹ] No dependencies declared.")
    except Exception as e:
        print(f"[!] Failed to install dependencies: {e}")

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return
    parser = argparse.ArgumentParser(description="Add or delete CLI command folders", add_help=False)
    parser.add_argument('--add', help="Path to a ZIP archive containing the command folder")
    parser.add_argument('--with-deps', action='store_true', help="Automatically install dependencies from manifest")
    parser.add_argument('--del', dest="del_command", help="Name of the command folder to delete")
    parser.add_argument('--allow-insecure', action='store_true',
        help="Allow commands with pip/subprocess install (not recommended)")
    args = parser.parse_args(argv)

    commands_dir = Path(cptd_tools.commands.__file__).parent

    if args.add:
        is_url = args.add.lower().startswith(("http://", "https://"))
        if is_url:
            tmp_zip = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")
            try:
                print(f"[⇩] Downloading from: {args.add}")
                urllib.request.urlretrieve(args.add, tmp_zip.name)
                zip_path = Path(tmp_zip.name)
                command_name = Path(urllib.parse.urlparse(args.add).path).stem
            except Exception as e:
                print(f"[!] Failed to download: {e}")
                return
        else:
            zip_path = Path(args.add)
            if not zip_path.exists() or not zip_path.name.endswith(".zip"):
                print("[!] Please provide a valid .zip archive or URL.")
                return
            command_name = zip_path.stem

        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref, tempfile.TemporaryDirectory() as temp_dir:
            zip_ref.extractall(temp_dir)
            temp_path = Path(temp_dir)
            try:
                manifest = _load_manifest(temp_path)
                if not is_compatible(manifest):
                    print(f"[⛔] '{command_name}' not installed: requires {manifest.get('target')}, "
                          f"current OS is {platform.system()}.")
                    return
            except Exception as e:
                print(f"[!] Error reading manifest: {e}")
                return

        target_dir = commands_dir / command_name
        if target_dir.exists():
            print(f"[!] Command folder '{command_name}' already exists.")
            return

        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir)

            if contains_forbidden_code(target_dir, allow_insecure=args.allow_insecure):
                shutil.rmtree(target_dir)
                print("[!] Aborted. Command folder removed.")
                return

            manifest_file = None
            for ext in ('yaml', 'json'):
                candidate = target_dir / f"manifest.{ext}"
                if candidate.exists():
                    manifest_file = candidate
                    break

            if not manifest_file:
                print("[!] No manifest file found. Expected manifest.yaml or manifest.json.")
                shutil.rmtree(target_dir)
                return

            manifest = load_manifest(manifest_file)
            print(f"[✓] Command '{command_name}' added.")
            print(f"📄 Description: {manifest.get('description', '-')}")
            print(f"🔰 Entrypoint : {manifest.get('entrypoint', '-')}")
            print(f"👤 Author     : {manifest.get('author', '-')}")

            install_dependencies_from_manifest(manifest_file, auto_confirm=args.with_deps)

        except Exception as e:
            print(f"[!] Error during import: {e}")
            if target_dir.exists():
                shutil.rmtree(target_dir)

    elif args.del_command:
        target = commands_dir / args.del_command
        if not target.exists() or not target.is_dir():
            print(f"[!] No such command folder: {args.del_command}")
            return
        if args.del_command == "command":
            print("[!] You cannot delete the 'command' command.")
            return
        shutil.rmtree(target)
        print(f"[✓] Command folder deleted: {args.del_command}")

    else:
        print("[!] Please specify either --add <zip> or --del <name>")

if __name__ == "__main__":
    run(sys.argv[1:])