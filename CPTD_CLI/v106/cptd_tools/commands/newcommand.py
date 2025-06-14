# newcommand.py — генерирует шаблон команды и два манифеста

import sys
import json
from pathlib import Path
from textwrap import dedent
from cptd_tools.syntax_utils import print_help

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


def generate_yaml_manifest(name: str) -> str:
    return dedent(f"""\
        name: {name}
        description: Опишите, что делает команда
        version: 1.0.0
        entrypoint: {name}.py
        dependencies:
          - colorama

        author: Асбйорн Расен
        email: asbjorn@example.com
        github: https://github.com/asbjornrasen
        website: https://asbjornrasen.dev
        license: license.md
    """)


def generate_json_manifest(name: str) -> str:
    return json.dumps({
        "name": name,
        "description": "Опишите, что делает команда",
        "version": "1.0.0",
        "entrypoint": f"{name}.py",
        "dependencies": ["colorama"],
        "author": "Асбйорн Расен",
        "email": "asbjorn@example.com",
        "github": "https://github.com/asbjornrasen",
        "website": "https://asbjornrasen.dev",
        "license": "license.md"
    }, indent=2, ensure_ascii=False)


def run(argv):
    if len(argv) != 2 or argv[0] != "--name":
        print("Usage: cptd newcommand --name yourcommand")
        return

    name = argv[1]
    py_file = Path(f"{name}.py")
    yaml_file = Path("manifest.yaml")
    json_file = Path("manifest.json")

    if py_file.exists():
        print(f"[!] File already exists: {py_file}")
        return

    with open(py_file, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(name=name))

    with open(yaml_file, "w", encoding="utf-8") as f:
        f.write(generate_yaml_manifest(name))

    with open(json_file, "w", encoding="utf-8") as f:
        f.write(generate_json_manifest(name))

    print(f"[✔] Command template created: {py_file}")
    print(f"[✔] Manifest created     : {yaml_file}")
    print(f"[✔] Manifest created     : {json_file}")
