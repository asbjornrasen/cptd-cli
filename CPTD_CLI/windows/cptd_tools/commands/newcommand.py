# newcommand.py — генерирует шаблон команды в текущем каталоге

import sys
from pathlib import Path
from textwrap import dedent
from cptd_tools.syntax_utils import print_help  # для совместимости с CLI

TEMPLATE = """
# {name}.py — CPTD CLI Command

from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

SYNTAX = {{
    "name": "{name}",
    "description": "Describe what this command does.",
    "usage": "cptd {name} --input <path> [--flag]",
    "arguments": [
        {{
            "name": "--input",
            "required": True,
            "help": "Path to the input file or folder"
        }},
        {{
            "name": "--flag",
            "required": False,
            "help": "Optional flag to control behavior"
        }}
    ],
    "examples": [
        "cptd {name} --input file.cptd",
        "cptd {name} --input folder --flag"
    ]
}}

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser(description=SYNTAX["description"], add_help=False)
    parser.add_argument('--input', type=Path, required=True, help='Path to the input file or folder')
    parser.add_argument('--flag', action='store_true', help='Optional flag')

    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {{e}}")
        print_help(SYNTAX)
        return

    if not args.input.exists():
        print(f"[!] Input path does not exist:\\n    {{args.input}}")
        return

    print(f"[✔] Processing input: {{args.input}}")
    if args.flag:
        print("[✔] Flag is set.")
""".lstrip()


def run(argv):
    if len(argv) != 2 or argv[0] != "--name":
        print("Usage: cptd newcommand --name yourcommand")
        return

    name = argv[1]
    filename = f"{name}.py"
    target_path = Path.cwd() / filename  # <-- создаём в текущем каталоге

    if target_path.exists():
        print(f"[!] File already exists: {filename}")
        return

    code = TEMPLATE.format(name=name)

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"[✔] Command template created in current folder: {target_path}")
