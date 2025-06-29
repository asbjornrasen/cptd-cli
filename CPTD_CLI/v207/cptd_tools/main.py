import argparse
import sys
import importlib.util
import json
import yaml
from pathlib import Path
from datetime import datetime
from cptd_tools.paths import HISTORY_FILE, SETTINGS_FILE


def get_history_line_limit():
    if SETTINGS_FILE.exists():
        try:
            with SETTINGS_FILE.open("r", encoding="utf-8") as f:
                settings = json.load(f)
                return int(settings.get("history_line_limit", 10000))
        except Exception as e:
            print(f"[!] Failed to read settings.json: {e}")
    return 10000  # default fallback

def enforce_history_limit():
    line_limit = get_history_line_limit()
    if not HISTORY_FILE.exists():
        HISTORY_FILE.touch()  
        return
    lines = HISTORY_FILE.read_text(encoding="utf-8").splitlines()
    if len(lines) > line_limit:
        lines = lines[-line_limit:]
        HISTORY_FILE.write_text("\n".join(lines), encoding="utf-8")


def log_history(command_line: str):
    timestamp = datetime.now().isoformat(timespec="seconds")
    with HISTORY_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {command_line}\n")
    enforce_history_limit()

# 📁 Каталог команд
BASE_COMMANDS_PATH = Path(__file__).parent / "commands"

def load_manifest_generic(command_path: Path) -> dict | None:
    for ext in ("yaml", "json"):
        manifest_path = command_path / f"manifest.{ext}"
        if manifest_path.exists():
            try:
                if ext == "yaml":
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        return yaml.safe_load(f)
                else:
                    with open(manifest_path, "r", encoding="utf-8") as f:
                        return json.load(f)
            except Exception as e:
                print(f"[!] Error reading manifest in {command_path.name}: {e}")
    return None

def list_available_commands():
    result = []
    for p in BASE_COMMANDS_PATH.iterdir():
        if not p.is_dir():
            continue
        manifest = load_manifest_generic(p)
        if not manifest:
            continue
        entrypoint = manifest.get("entrypoint", "main.py")
        entry_file = p / entrypoint
        if not entry_file.exists():
            result.append(f"❌ {p.name} — missing entrypoint: {entrypoint}")
        else:
            desc = manifest.get("description", "")
            result.append(f"✅ {p.name} — {desc}")
    return result

def main():
    
    if len(sys.argv) == 1:
        print("\n[ℹ] Usage: cptd <command> [args]")
        print("     Run `cptd list` to see all available commands.")
        return

    parser = argparse.ArgumentParser(prog='cptd', description='CPTD CLI Tool', add_help=False)
    parser.add_argument('command', help='commands (list, or folder name)')
    args, unknown = parser.parse_known_args()

    if args.command == 'list':
        print("\n Available commands:")
        for line in list_available_commands():
            print(f"  - {line}")
        return

    command_dir = BASE_COMMANDS_PATH / args.command
    manifest = load_manifest_generic(command_dir)
    if not manifest:
        print(f"[!] No valid manifest found in: {args.command}")
        return

    entrypoint = manifest.get("entrypoint", "main.py")
    entry_file = command_dir / entrypoint

    if not entry_file.exists():
        print(f"[!] Entrypoint '{entrypoint}' not found in {args.command}")
        return

    spec = importlib.util.spec_from_file_location(f"cptd_command_{args.command}", entry_file)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(command_dir))  
    spec.loader.exec_module(module)

    
    log_history(f"{args.command} {' '.join(unknown)}")

    if hasattr(module, "run"):
        module.run(unknown)
    else:
        print(f"[!] No 'run' function found in '{entrypoint}'")

if __name__ == '__main__':
    main()
