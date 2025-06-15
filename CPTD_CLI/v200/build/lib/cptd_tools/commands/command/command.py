# cptd_tools/commands/command.py

import argparse
import shutil
import subprocess
import sys
import json
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml"], check=True)
    import yaml

import cptd_tools.commands

SYNTAX = {
    "name": "command",
    "description": "Add or delete CLI command folders into the CPTD DSL system",
    "usage": "cptd command --add <file.zip> [--with-deps] | --del <command_name>",
    "arguments": [
        {"name": "--add", "required": False, "help": "ZIP archive of the command folder to add"},
        {"name": "--with-deps", "required": False, "help": "Automatically install dependencies from manifest"},
        {"name": "--del", "required": False, "help": "Command folder name to delete"}
    ],
    "examples": [
        "cptd command --add mycommand.zip --with-deps",
        "cptd command --del mycommand"
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

def contains_forbidden_code(dir_path: Path) -> bool:
    for py_file in dir_path.rglob("*.py"):
        content = py_file.read_text(encoding='utf-8')
        if 'pip install' in content or 'subprocess' in content and 'install' in content:
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
    parser = argparse.ArgumentParser(description="Add or delete CLI command folders")
    parser.add_argument('--add', help="Path to a ZIP archive containing the command folder")
    parser.add_argument('--with-deps', action='store_true', help="Automatically install dependencies from manifest")
    parser.add_argument('--del', dest="del_command", help="Name of the command folder to delete")
    args = parser.parse_args(argv)

    commands_dir = Path(cptd_tools.commands.__file__).parent

    if args.add:
        zip_path = Path(args.add)
        if not zip_path.exists() or not zip_path.name.endswith(".zip"):
            print("[!] Please provide a valid .zip archive.")
            return

        command_name = zip_path.stem
        target_dir = commands_dir / command_name
        if target_dir.exists():
            print(f"[!] Command folder '{command_name}' already exists.")
            return

        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_dir)

            if contains_forbidden_code(target_dir):
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
        print(f"[−] Command folder deleted: {args.del_command}")

    else:
        print("[!] Please specify either --add <zip> or --del <name>")
