# cptd_tools/commands/command.py

import argparse
import shutil
import subprocess
import sys
import json
import pkgutil
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[•] Missing dependency: pyyaml. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml"], check=True)
    import yaml

import cptd_tools.commands

SYNTAX = {
    "name": "command",
    "description": "Add or delete CLI command files into the CPTD DSL system",
    "usage": "cptd command --add <file.py> [--with-deps] | --del <file.py>",
    "arguments": [
        {"name": "--add", "required": False, "help": "Path to the .py file to copy into the CLI command set"},
        {"name": "--with-deps", "required": False, "help": "Automatically install dependencies from manifest"},
        {"name": "--del", "required": False, "help": "Name of the .py file to delete from installed commands"}
    ],
    "examples": [
        "cptd command --add mycommand.py",
        "cptd command --add mycommand.py --with-deps",
        "cptd command --del mycommand.py"
    ]
}

def install_dependencies_from_manifest(manifest_path: Path):
    try:
        manifest = load_manifest(manifest_path)
        deps = manifest.get("dependencies", [])
        if deps:
            print(f"[•] Installing dependencies: {', '.join(deps)}")
            subprocess.run([sys.executable, "-m", "pip", "install", *deps], check=True)
        else:
            print("[ℹ] No dependencies found in manifest.")
    except Exception as e:
        print(f"[!] Failed to install dependencies: {e}")

def load_manifest(manifest_path: Path) -> dict:
    if manifest_path.suffix == '.yaml':
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    elif manifest_path.suffix == '.json':
        with open(manifest_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported manifest format: {manifest_path.name}")

def display_author_info(manifest: dict):
    print()
    if "author" in manifest:
        print(f"👤 Author   : {manifest['author']}")
    if "email" in manifest:
        print(f"📧 Email    : {manifest['email']}")
    if "github" in manifest:
        print(f"🌐 GitHub   : {manifest['github']}")
    if "website" in manifest:
        print(f"🔗 Website  : {manifest['website']}")
    if "license" in manifest:
        print(f"🔑 License  : {manifest['license']}")
    print()

def contains_forbidden_install_code(py_file: Path) -> bool:
    with open(py_file, encoding='utf-8') as f:
        content = f.read()
    forbidden_snippets = [
        'subprocess.run([sys.executable, "-m", "pip", "install"',
        'subprocess.call([sys.executable, "-m", "pip", "install"',
    ]
    return any(snippet in content for snippet in forbidden_snippets)


def run(argv):
    parser = argparse.ArgumentParser(description="Add or delete CLI command files")
    parser.add_argument('--add', help="Path to the .py file to add")
    parser.add_argument('--with-deps', action='store_true', help="Automatically install dependencies from manifest")
    parser.add_argument('--del', dest="del_command", help="Name of the command file to delete")
    args, extra = parser.parse_known_args(argv)


    commands_dir = Path(cptd_tools.commands.__file__).parent

    if args.add:
        src = Path(args.add)
        if not src.exists() or not src.is_file():
            print(f"[!] File not found: {src}")
            return
        if not src.name.endswith(".py"):
            print("[!] Only .py files are allowed")
            return
        
        if contains_forbidden_install_code(src):
            print(f"[⛔] Forbidden code detected in '{src.name}': auto-installation of modules is not allowed.")
            print("    Please remove dynamic installation code (e.g., pip install) and use a manifest instead.")
            return


        dest = commands_dir / src.name
        shutil.copy(src, dest)
        print(f"[✓] Command \"{src.stem}\" successfully added to: {dest}")

        # Поиск манифеста
        manifest_yaml = src.with_name("manifest.yaml")
        manifest_json = src.with_name("manifest.json")
        manifest_file = manifest_yaml if manifest_yaml.exists() else manifest_json if manifest_json.exists() else None

        if manifest_file:
            try:
                manifest = load_manifest(manifest_file)

                # Проверка entrypoint
                entrypoint = manifest.get("entrypoint", "")
                if entrypoint and entrypoint != src.name:
                    print(f"[!] ⚠️ Manifest entrypoint is '{entrypoint}', but you added '{src.name}'")

                # Установка зависимостей
                if args.with_deps:
                    install_dependencies_from_manifest(manifest_file)
                else:
                    answer = input(f"[?] Found {manifest_file.name}. Install dependencies? [Y/n]: ").strip().lower()
                    if answer in ("", "y", "yes"):
                        install_dependencies_from_manifest(manifest_file)

                # Отображение автора
                display_author_info(manifest)

            except Exception as e:
                print(f"[!] Could not read manifest: {e}")

    elif args.del_command:
        target = commands_dir / args.del_command
        if not target.exists():
            print(f"[!] No such command: {target}")
            return
        if target.name == "command.py":
            print("[!] You cannot delete the 'command' command.")
            return
        target.unlink()
        print(f"[-] Command deleted: {target}")

    elif '--list' in extra:
        print("\n Available commands:")
        for _, name, _ in pkgutil.iter_modules(cptd_tools.commands.__path__):
            print(f"  - {name}")
        print()


    else:
        print("[!] Please specify either --add or --del.")


