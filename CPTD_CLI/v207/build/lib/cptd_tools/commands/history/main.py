import argparse
from pathlib import Path
import sys
import json
from cptd_tools.paths import HISTORY_FILE, SETTINGS_FILE


# HISTORY_FILE = Path(__file__).resolve().parents[2] / "history.txt"
# SETTINGS_FILE = Path(__file__).resolve().parents[2] / "settings.json"   

SYNTAX = {
    "name": "history",
    "description": "View, search, clear, or export the CPTD CLI command history",
    "usage": "cptd history --show [--grep text] [--export path] [--head N] | --clear | --settings [--line N]",
    "arguments": [
        {"name": "--show", "required": False, "help": "Show history entries"},
        {"name": "--grep", "required": False, "help": "Filter entries containing text (case-insensitive)"},
        {"name": "--export", "required": False, "help": "Export history to the specified file"},
        {"name": "--head", "required": False, "help": "Show only the last N entries"},
        {"name": "--clear", "required": False, "help": "Clear the history"},
        {"name": "--settings", "required": False, "help": "Adjust or view history settings"},
        {"name": "--line", "required": False, "help": "Set max number of lines in history"}
    ],
    "examples": [
        "cptd history --show",
        "cptd history --show --grep install",
        "cptd history --show --head 20",
        "cptd history --export myhistory.txt",
        "cptd history --clear",
        "cptd history --settings --line 5000",
        "cptd history --settings"
    ]
}

def print_help():
    print(f"\nUsage: {SYNTAX['usage']}")
    print(f"\nDescription: {SYNTAX['description']}")
    print("\nArguments:")
    for arg in SYNTAX['arguments']:
        print(f"  {arg['name']}\t{arg['help']}")
    print("\nExamples:")
    for ex in SYNTAX['examples']:
        print(f"  {ex}")

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help()
        return

    parser = argparse.ArgumentParser(prog='cptd history', add_help=False)
    parser.add_argument('--show', action='store_true', help='Show history entries')
    parser.add_argument('--grep', type=str, help='Filter entries containing text')
    parser.add_argument('--export', type=Path, help='Export history to the specified file')
    parser.add_argument('--head', type=int, help='Show only the last N entries')
    parser.add_argument('--clear', action='store_true', help='Clear the history')
    parser.add_argument('--settings', action='store_true', help='Adjust or view history settings')
    parser.add_argument('--line', type=int, help='Set max number of lines in history')

    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help()
        return

    if args.settings:
        if args.line:
            settings = {}
            if SETTINGS_FILE.exists():
                try:
                    with SETTINGS_FILE.open("r", encoding="utf-8") as f:
                        settings = json.load(f)
                except Exception as e:
                    print(f"[!] Failed to load settings.json: {e}")
            settings["history_line_limit"] = args.line
            with SETTINGS_FILE.open("w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2)
            print(f"[✔] History line limit set to {args.line}")
        else:
            if SETTINGS_FILE.exists():
                try:
                    with SETTINGS_FILE.open("r", encoding="utf-8") as f:
                        settings = json.load(f)
                        print(f"[ℹ] Current history line limit: {settings.get('history_line_limit', 10000)}")
                except Exception as e:
                    print(f"[!] Failed to load settings.json: {e}")
            else:
                print("[ℹ] No settings found, default limit is 10000 lines")
        return

    if args.clear:
        HISTORY_FILE.write_text("")
        print("[✔] History cleared.")
        return

    if not HISTORY_FILE.exists():
        print("[!] No history file found.")
        return

    content = [line.strip() for line in HISTORY_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]

    if args.grep:
        content = [line for line in content if args.grep.lower() in line.lower()]

    if args.head:
        content = content[-args.head:]

    if args.export:
        args.export.write_text("\n".join(content), encoding="utf-8")
        print(f"[✔] History exported to {args.export}")
        return

    if args.show:
        if content:
            print("\n[📜] Command History:")
            for line in content:
                print(f"  {line}")
        else:
            print("[ℹ] History is empty.")
        return

    print_help()
