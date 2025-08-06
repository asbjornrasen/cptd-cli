# cptd_tools/commands/about.py

import cptd_tools
from pathlib import Path
from cptd_tools.syntax_utils import print_help
import sys

SYNTAX = {
    "name": "about",
    "description": "Show CPTD manifest information.",
    "usage": "cptd about",
    "arguments": [],
    "examples": [
        "cptd about"
    ]
}

MANIFEST_FILE = Path(cptd_tools.__file__).parent / "cptd_manifest.cptd"


def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    if not MANIFEST_FILE.exists():
        print("[!] Manifest file not found:", MANIFEST_FILE)
        return

    print("📦 CPTD MANIFEST\n")
    for line in MANIFEST_FILE.read_text(encoding="utf-8").splitlines():
        if line.strip():
            print("  ", line)

    print("\n[✔] Manifest loaded from:", MANIFEST_FILE)

if __name__ == "__main__":
    run(sys.argv[1:])
