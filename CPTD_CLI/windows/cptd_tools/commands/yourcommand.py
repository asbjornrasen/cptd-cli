# yourcommand.py — CPTD CLI Command Template

from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

# ──────────────────────────────────────────────────────────────
# SYNTAX BLOCK: used for --help and documentation generation
# ──────────────────────────────────────────────────────────────

SYNTAX = {
    "name": "yourcommand",
    "description": "Short description of what this command does.",
    "usage": "cptd yourcommand [options]",
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
        "cptd yourcommand --input myfile.cptd",
        "cptd yourcommand --input folder --flag"
    ]
}

# ──────────────────────────────────────────────────────────────
# Main logic
# ──────────────────────────────────────────────────────────────

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    # ✅ Отключаем встроенный argparse-help
    parser = argparse.ArgumentParser(description=SYNTAX["description"], add_help=False)
    parser.add_argument('--input', type=Path, required=True, help='Path to the input file or folder')
    parser.add_argument('--flag', action='store_true', help='Optional flag to control behavior')

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
