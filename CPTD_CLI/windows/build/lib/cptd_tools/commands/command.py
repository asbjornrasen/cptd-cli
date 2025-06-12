# cptd_tools/commands/command.py

import argparse
import shutil
from pathlib import Path
import cptd_tools.commands  # нужен для нахождения установленной директории

SYNTAX = {
    "name": "command",
    "description": "Add or delete CLI command files into the CPTD DSL system",
    "usage": "cptd command --add <file.py> | --del <file.py>",
    "arguments": [
        {
            "name": "--add",
            "required": False,
            "help": "Path to the local .py file to copy into the CLI command set"
        },
        {
            "name": "--del",
            "required": False,
            "help": "Name of the .py file to delete from installed commands"
        }
    ],
    "examples": [
        "cptd command --add mycommand.py",
        "cptd command --del mycommand.py"
    ]
}

def run(argv):
    parser = argparse.ArgumentParser(description="Add or delete CLI command files")
    parser.add_argument('--add', help="Path to the .py file to add")
    parser.add_argument('--del', dest="del_command", help="Name of the command file to delete")
    args = parser.parse_args(argv)

    commands_dir = Path(cptd_tools.commands.__file__).parent

    if args.add:
        src = Path(args.add)
        if not src.exists() or not src.is_file():
            print(f"[!] File not found: {src}")
            return
        if not src.name.endswith(".py"):
            print("[!] Only .py files are allowed")
            return
        dest = commands_dir / src.name
        shutil.copy(src, dest)
        print(f"[+] Command added to: {dest}")

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

    else:
        print("[!] Please specify either --add or --del.")
