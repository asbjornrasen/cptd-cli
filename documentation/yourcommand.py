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