# test.py — CPTD CLI Command

from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "test",
    "description": "Describe what this command does.",
    "usage": "cptd test --input <path> [--flag]",
    "arguments": [
        {
            "name": "--input",
            "required": True,
            "help": "Path to the input file or folder"
        },
        {
            "name": "--flag",
            "required": False,
            "help": "Optional flag to control behavior"
        }
    ],
    "examples": [
        "cptd test --input file.cptd",
        "cptd test --input folder --flag"
    ]
}

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
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    if not args.input.exists():
        print(f"[!] Input path does not exist:\n    {args.input}")
        return

    print(f"[✔] Processing input: {args.input}")
    if args.flag:
        print("[✔] Flag is set.")
