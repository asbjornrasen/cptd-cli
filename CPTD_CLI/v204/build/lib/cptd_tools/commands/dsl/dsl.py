# cptd_tools/commands/dsl.py

from pathlib import Path
import argparse
import shutil
import json
import sys
from datetime import datetime
from cptd_tools.syntax_utils import print_help
import re

SYNTAX = {
    "name": "dsl",
    "description": "Manage CPTD DSL files and tasks (add, delete, archive, initialize, etc).",
    "usage": "cptd dsl [--add <text> | --del <query> | --arch <query> | --init | --dashboard | --setpath <path> | --delpatch | --path]",
    "arguments": [
        {"name": "--add", "required": False, "help": "Add line to active_cptd.md."},
        {"name": "--del", "required": False, "help": "Delete line matching id or phrase."},
        {"name": "--arch", "required": False, "help": "Archive line matching id or phrase. If not set, all [X] except habits are archived."},
        {"name": "--init", "required": False, "help": "Initialize project structure."},
        {"name": "--dashboard", "required": False, "help": "Show goals and tasks overview."},
        {"name": "--setpath", "required": False, "help": "Save CPTD base path."},
        {"name": "--delpatch", "required": False, "help": "Remove the saved setpath file."},
        {"name": "--path", "required": False, "help": "Show current saved CPTD base path."},
    ],
    "examples": [
        "cptd dsl --add '[X] task:example id:T001'",
        "cptd dsl --del T001",
        "cptd dsl --arch T001",
        "cptd dsl --arch",
        "cptd dsl --init",
        "cptd dsl --dashboard",
        "cptd dsl --setpath ~/Documents/cptd",
        "cptd dsl --delpatch",
        "cptd dsl --path"
    ]
}

CONFIG_PATH = Path.home() / ".cptd_config.json"


def get_base_dir():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Path(data.get("base_path", "."))
    return Path.cwd()


def modify_file(file_path: Path, predicate, action="remove"):
    """Переносит/удаляет строки по предикату.

    action = "keep"   → строка остаётся в исходном файле  
    action = "remove" → строка вырезается из исходного файла
    """
    lines  = file_path.read_text(encoding="utf-8").splitlines()
    result, moved = [], []

    for line in lines:
        if predicate(line):
            moved.append(line)
            if action == "keep":
                result.append(line)
        else:
            result.append(line)

    file_path.write_text("\n".join(result) + "\n", encoding="utf-8")
    return moved




def dashboard(base: Path):
    def parse_manifest(path: Path):
        return {k.strip().lower(): v.strip()
                for k, v in (l.split(':', 1)
                             for l in path.read_text(encoding="utf-8", errors="ignore").splitlines()
                             if ':' in l)}

    def fields_dict(line: str):
        return {k.lower(): v.strip() for k, v in re.findall(r"(\w+):\s*([^:\n]+?)(?=\s+\w+:|$)", line)}

    def parse_goals_structure(text):
        goals, goal, project = [], None, None
        for raw in text.splitlines():
            f = fields_dict(raw)
            l = raw.lower()
            if "goals:" in l:
                goal = {"raw": raw, "fields": f, "projects": []}
                goals.append(goal)
            elif "project:" in l and goal:
                project = {"raw": raw, "fields": f, "tasks": []}
                goal["projects"].append(project)
            elif "task:" in l and project:
                project["tasks"].append({"raw": raw, "fields": f})
        return goals

    def parse_active_tasks(text):
        future, daily = [], []
        for m in re.finditer(r".*task:.*", text, re.IGNORECASE):
            raw = m.group(0)
            f = fields_dict(raw)
            block = future if "FUTURE" in text[max(0, m.start()-80):m.start()].upper() else daily
            block.append({"raw": raw, "fields": f})
        return {"future": future, "daily": daily}

    def fmt_task(raw: str, fields: dict, indent: int = 0):
        prefix = ""
        m = re.match(r"^\s*(\[[^\]]*\]\s*\[[^\]]*\])", raw)
        if m:
            prefix = m.group(1).strip() + " "
        ordered = []
        field_order = ['depends_on', 'task', 'start', 'due', 'end', 'place', 'method', 'role', 'tags', 'id']
        for key in field_order:
            if key in fields:
                ordered.append(f"{key}: {fields[key]}")
        for k, v in fields.items():
            if k not in field_order:
                ordered.append(f"{k}: {v}")
        return " " * indent + prefix + " | ".join(ordered)

    goals_file = base / "goals_cptd.md"
    active_file = base / "active_cptd.md"
    manifest_file = base / "user_manifest.cptd"

    if not all(p.exists() for p in (goals_file, active_file, manifest_file)):
        print("[!] Required files missing for dashboard.")
        return

    manifest = parse_manifest(manifest_file)
    goals = parse_goals_structure(goals_file.read_text(encoding="utf-8", errors="ignore"))
    active = parse_active_tasks(active_file.read_text(encoding="utf-8", errors="ignore"))

    print(" USER INFO")
    print(f"Name     : {manifest.get('name', '')}")
    print(f"Email    : {manifest.get('email', '')}")
    print(f"Role     : {manifest.get('role', '')}")
    print(f"Created  : {manifest.get('created', '')}\n")

    for g in goals:
        gid = g['fields'].get('id', '')
        gname = g['fields'].get('goals', '')
        print(f" GOAL: {gid} — {gname}\n")
        for p in g['projects']:
            pid = p['fields'].get('id', '')
            pname = p['fields'].get('project', '')
            print(f"   PROJECT: {pid} — {pname}")
            for t in p['tasks']:
                print(fmt_task(t['raw'], t['fields'], indent=4))
            print()

    print(" FUTURE TASKS")
    for t in active["future"]:
        print(fmt_task(t['raw'], t['fields']))
    print("\n DAILY TASKS")
    for t in active["daily"]:
        print(fmt_task(t['raw'], t['fields']))
    print()


def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--add")
    parser.add_argument("--del")
    parser.add_argument("--arch", nargs="?")  
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--dashboard", action="store_true")
    parser.add_argument("--setpath")
    parser.add_argument("--delpatch", action="store_true")
    parser.add_argument("--path", action="store_true")
    args = parser.parse_args(argv)

    base = get_base_dir()
    active_file = base / "active_cptd.md"
    archive_file = base / "archive_cptd.md"

    if args.path:
        if CONFIG_PATH.exists():
            print(" Saved base path:", get_base_dir().resolve())
        else:
            print("[!] No path saved. Using current directory:", Path.cwd())
        return

    if args.setpath:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump({"base_path": str(Path(args.setpath).resolve())}, f)
        print(f"[✔] Path saved: {args.setpath}")
        return

    if args.delpatch:
        CONFIG_PATH.unlink(missing_ok=True)
        print("[✔] setpath deleted.")
        return

    if args.init:
        today_str = datetime.today().strftime('%Y-%m-%d')
        files_to_create = {
            "goals_cptd.md": (
                "# Goals\n\n"
                "[][A]goals:Example of a goal id:G001 progress:0/1\n"
                "   [][A]project:Example of a goal id:G001_P01 progress:0/1\n"
                "       [][A]task:Example of a goal id:G001_P01_T01 \n"
            ),
            "archive_cptd.md": "# Goals Archive\n\n",
            "active_cptd.md": (
                "# Active Tasks\n\n"
                "[status][priority] depends_on:<TaskID> task:Task Name start:2025-06-13 due:2025-06-20 end: place:Location method:Tool role:role,name tags:tag1,tag2 id:G001_P001_T001\n"
            ),
            "user_manifest.cptd": (
                "## CPTD USER Manifest\n\n"
                "schema: CPTD-DSL-2\n"
                "encoding: UTF-8\n"
                f"created: {today_str}\n"
                "name: \n"
                "email: \n"
            ),
        }
        print(f"\n Initializing the CPTD project in: {base.resolve()}\n")
        for filename, content in files_to_create.items():
            file_path = base / filename
            if file_path.exists():
                print(f"  {filename} already exists - skipped")
            else:
                file_path.write_text(content, encoding="utf-8")
                print(f" File created: {filename}")
        print("\n CPTD initialization complete. Ready to plan your goals.")
        return

    if args.dashboard:
        dashboard(base)
        return

    if args.add:
        line = args.add.strip()
        with open(active_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")
        print(f"[+] Added to active: {line}")
        return

    if args.__dict__["del"]:
        query = args.__dict__["del"]
        moved = modify_file(active_file, lambda l: query in l, action="remove")
        print(f"[x] Deleted lines matching '{query}': {len(moved)}")
        return

    # ─────────────────── архивирование ───────────────────────────
    if "--arch" in argv:
        query = args.arch.strip() if args.arch else None

        if query:
            predicate = lambda l: query in l
        else:
            # [X] или [X][A], [X][B], и т.п.
            predicate = lambda l: re.match(r"^\[X\](\[\w\])?", l.strip()) and "habit:" not in l




        moved = modify_file(active_file, predicate, action="remove")

        if moved:
            with open(archive_file, "a", encoding="utf-8") as f:
                f.write("\n".join(moved) + "\n")

        print(f"[→] Archived lines: {len(moved)}")
        return

