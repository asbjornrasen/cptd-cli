#setpath.py

# setpath.py

import json
from pathlib import Path
from cptd_tools.syntax_utils import print_help, parse_args

# ──────────────────────────────────────────────────────────────
# SYNTAX BLOCK: used for --help and documentation generation
# ──────────────────────────────────────────────────────────────

SYNTAX = {
    "name": "setpath",
    "description": "Save the base directory path for all CPTD files (e.g., goals, logs).",
    "usage": "cptd setpath <base_path>",
    "arguments": [
        {
            "name": "<base_path>",
            "required": True,
            "help": "Path to the folder containing your CPTD files"
        }
    ],
    "examples": [
        "cptd setpath ~/Documents/cptd",
        "cptd setpath /mnt/data/plans"
    ]
}

# ──────────────────────────────────────────────────────────────
# Main logic
# ──────────────────────────────────────────────────────────────

CONFIG_PATH = Path.home() / '.cptd_config.json'

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    args = parse_args(argv, SYNTAX)
    base_path = Path(args["<base_path>"]).expanduser()

    if not base_path.exists():
        print("[!] The specified path does not exist.")
        return

    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump({"base_path": str(base_path)}, f)

    print(f"[✔] Base path saved:\n {base_path}")
