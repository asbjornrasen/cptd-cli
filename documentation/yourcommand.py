# yourcommand.py — CPTD CLI Command Template
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
        {"name": "--flag", "required": False, "help": "Optional flag"}
    ],
    "examples": [
        "cptd yourcommand --input file.cptd",
        "cptd yourcommand --input folder --flag"
    ]
}

def run(argv):
    # The mandatory argument "add_help=False" disables argparse help and enables cptd help
    prs = argparse.ArgumentParser("cptd yourcommand", add_help=False)

    # Adding arguments
    prs.add_argument('--input', type=Path, required=True, help='Path to input file')
    prs.add_argument('--flag', action='store_true', help='Optional flag')

    # Check if --help or -h is passed
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    try:
        args = prs.parse_args(argv)
    except argparse.ArgumentError as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    # If the --input argument is passed
    if args.input:
        print(f"[✔] Path provided: {args.input}")
        print(f"  Example of how to call this script with this argument: cptd yourcommand --input {args.input}")

    # If the --flag argument is passed
    if args.flag:
        print("[✔] Flag is set")

    # Checking file existence
    if not args.input.exists():
        print(f"[!] Path does not exist:\n    {args.input}")
        return

    print(f"[✔] Processing: {args.input}")

if __name__ == "__main__":
    run(sys.argv[1:])