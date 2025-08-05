# newcommand.py — генератор примеров команды CPTD

import sys
import json
from pathlib import Path
from textwrap import dedent
import cptd_tools
from cptd_tools.syntax_utils import print_help

TEMPLATE_MAIN = """
# main.py — CPTD CLI Command

import sys
from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "yourcommand",
    "description": "What the command does",
    "usage": "cptd yourcommand --input <path> [--flag]",
    "arguments": [
        {"name": "--input", "required": True, "help": "Path to input file"},
        {"name": "--flag", "required": False, "help": "Optional flag"},
        {"name": "--example", "required": False, "help": "Example mode"}
    ],
    "examples": [
        "cptd yourcommand --input file.cptd --flag",
        "cptd yourcommand --input file.cptd --example"
    ]
}

def run(argv):
    # The mandatory argument "add_help=False" disables argparse help and enables cptd help
    prs = argparse.ArgumentParser("cptd yourcommand", add_help=False)

    # Adding arguments
    prs.add_argument('--input', type=Path, required=True, help='Path to input file')
    prs.add_argument('--flag', action='store_true', help='Optional flag')
    prs.add_argument('--example', action='store_true', help='Optional flag')

    # Check if --help or -h is passed
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    try:
        args = prs.parse_args(argv)
    except SystemExit:
        print("[!] Argument parsing failed.")
        print_help(SYNTAX)
        return

    # If the --input argument is passed along with a value, for example: --input value, args.input evaluates to True and takes the value ,type=Path, type=str , type=int
    if args.input:
        print(f"[✔] Path provided: {args.input}")
     
    # If the --flag argument is passed without a value, action='store_true'
    if args.flag:
        print("[✔] Flag is set")
        
    # If the --example argument is passed without a value, action='store_true'
    if args.example:
        print("[✔] Example flag is set")
        
if __name__ == "__main__":
    run(sys.argv[1:])

""".strip()

TEMPLATE_SINGLE = '''
# main.py — CPTD CLI Command (Single-file version)

import argparse
from pathlib import Path
from cptd_tools.syntax_utils import print_help
import sys


SYNTAX = {
    "name": "yourcommand",
    "description": "Single-file CLI command with embedded logic",
    "usage": "cptd yourcommand --input <path> [--flag]",
    "arguments": [
        {
            "name": "--input",
            "required": True,
            "help": "Path to the input file or folder"
        },
        {
            "name": "--flag",
            "required": False,
            "help": "Optional flag"
        },
        {
            "name": "--example",
            "required": False,
            "help": "Optional flag for demonstration"
        }
    ],
    "examples": [
        "cptd yourcommand --input file.cptd",
        "cptd yourcommand --input folder --flag"
    ]
}

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser(description=SYNTAX["description"], add_help=False)
    parser.add_argument('--input', type=Path, required=True, help='Path to the input')
    parser.add_argument('--flag', action='store_true', help='Optional flag')
    parser.add_argument('--example', action='store_true', help='Optional flag')


    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    # If the --input argument is passed along with a value, for example: --input value, args.input evaluates to True and takes the value ,type=Path, type=str , type=int
    if args.input:
        print(f"[✔] Path provided: {args.input}")
     
    # If the --flag argument is passed without a value, action='store_true'
    if args.flag:
        print("[✔] Flag is set")
        
    # If the --example argument is passed without a value, action='store_true'
    if args.example:
        print("[✔] Example flag is set")

def process():
    print("[util.onecommand] Processing...")

def handle():
    print("[util.twocommand] Handling...")

def start():
    print("[service.onecommand] Service started.")

def end():
    print("[service.twocommand] Service ended.")

if __name__ == "__main__":
    run(sys.argv[1:])
'''.strip()


UTIL_ONE = """
def process():
    print("[util.onecommand] Processing...")
""".strip()

UTIL_TWO = """
def handle():
    print("[util.twocommand] Handling...")
""".strip()

SERVICE_ONE = """
def start():
    print("[service.onecommand] Service started.")
""".strip()

SERVICE_TWO = """
def end():
    print("[service.twocommand] Service ended.")
""".strip()

def generate_yaml_manifest() -> str:
    return dedent("""\
        name: yourcommand
        description: Demo CLI command with substructure
        version: 1.0.0
        target: all
        icon:
        entrypoint: main.py
        dependencies:
          - example
        author: example
        email: example@example.com
        github: https://github.com/example
        website: https://example.dev
        license: example.md
    """)

def generate_json_manifest() -> str:
    return json.dumps({
        "name": "yourcommand",
        "description": "Demo CLI command with substructure",
        "version": "1.0.0",
        "target": "all",
        "icon":"",
        "entrypoint": "main.py",
        "dependencies": ["example"],
        "author": "example",
        "email": "example@example.com",
        "github": "https://github.com/example",
        "website": "https://example.dev",
        "license": "example.md"
    }, indent=2, ensure_ascii=False)

def write_structure(base: Path, files: dict[str, str]):
    for rel_path, content in files.items():
        file_path = base / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

def create_examples():
    # Project_one — с корректным main.py
    base1 = Path("Project_one/yourcommand")
    write_structure(base1, {
        "main.py": TEMPLATE_SINGLE,
        "manifest.yaml": generate_yaml_manifest(),
        "manifest.json": generate_json_manifest(),
        "util/onecommand.py": UTIL_ONE,
        "util/twocommand.py": UTIL_TWO,
        "service/service_one.py": SERVICE_ONE,
        "service/service_two.py": SERVICE_TWO,
        "__init__.py": "",
        "util/__init__.py": "",
        "service/__init__.py": "",
    })

    # Project_two — заглушка
    base2 = Path("Project_two/yourcommand")
    write_structure(base2, {
        "main.py": TEMPLATE_MAIN,
        "manifest.yaml": generate_yaml_manifest(),
        "manifest.json": generate_json_manifest(),
        "__init__.py": ""
    })

def run(argv):
    if argv:
        print("[!] This command takes no arguments. Just run: cptd newcommand")
        return

    source_md = Path(cptd_tools.__file__).parent / "create_command.md"
    target_md = Path("create_command.md")
    print(f"[debug] Looking for guide at: {source_md.resolve()}")
    if source_md.exists():
        target_md.write_text(source_md.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"[✔] Guide copied         : {target_md}")
    else:
        print("[!] create_command.md not found. Skipping copy.")

    create_examples()
    print(f"[✔] Created: Project_one/yourcommand, Project_two/yourcommand")
