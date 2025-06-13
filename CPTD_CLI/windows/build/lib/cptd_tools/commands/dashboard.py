#dashboard.py

from __future__ import annotations
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict

GOALS_FILE = Path("goals_cptd.md")
ACTIVE_FILE = Path("activ_cptd.md")
MANIFEST_FILE = Path("user_manifest.cptd")

# ⬅️ Исправленный шаблон
GOAL_RE = re.compile(r"^#+\s*\[\]\[(\w)\]\s*goals:(?P<name>.+?)\s+id:(?P<gid>G\d+)", re.MULTILINE)
PROJECT_RE = re.compile(r"^\s*\[\]\[(\w)\]\s*project:(?P<name>.+?)\s+id:(?P<pid>G\d+_P\d+)", re.MULTILINE)
TASK_LINE_RE = re.compile(r"^\s*(\[[^\]]*\])(\[[^\]]*\])(?: depends_on:(\S+))?\s+task:(.+?)(?:\s+start:(\S+))?(?:\s+due:(\S+))?(?:\s+end:(\S+))?(?:\s+place:(\S+))?(?:\s+method:(\S+))?(?:\s+role:(\S+))?(?:\s+tags:(\S+))?\s+id:(G\d+_P\d+_T\d+)", re.MULTILINE)

def parse_manifest(file: Path) -> Dict[str, str]:
    data = {}
    if not file.exists():
        return data
    for line in file.read_text(encoding="utf-8").splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip()
    return data

def parse_goals_structure(text: str):
    lines = text.splitlines()
    goals = []
    goal = None
    project = None
    for line in lines:
        goal_match = GOAL_RE.match(line)
        project_match = PROJECT_RE.match(line)
        task_match = TASK_LINE_RE.match(line)

        if goal_match:
            goal = {
                "id": goal_match.group("gid"),
                "name": goal_match.group("name").strip(),
                "projects": []
            }
            goals.append(goal)

        elif project_match and goal:
            project = {
                "id": project_match.group("pid"),
                "name": project_match.group("name").strip(),
                "tasks": []
            }
            goal["projects"].append(project)

        elif task_match and project:
            task = {
                "status": task_match.group(1),
                "priority": task_match.group(2),
                "depends_on": task_match.group(3),
                "task": task_match.group(4).strip(),
                "start": task_match.group(5),
                "due": task_match.group(6),
                "end": task_match.group(7),
                "place": task_match.group(8),
                "method": task_match.group(9),
                "role": task_match.group(10),
                "tags": task_match.group(11),
                "id": task_match.group(12)
            }
            project["tasks"].append(task)
    return goals

def parse_active_tasks(text: str) -> Dict[str, List[str]]:
    future = []
    daily = []
    for m in TASK_LINE_RE.finditer(text):
        entry = {
            "status": m.group(1),
            "priority": m.group(2),
            "depends_on": m.group(3),
            "task": m.group(4).strip(),
            "start": m.group(5),
            "due": m.group(6),
            "end": m.group(7),
            "place": m.group(8),
            "method": m.group(9),
            "role": m.group(10),
            "tags": m.group(11),
            "id": m.group(12)
        }
        # Very simple split heuristic
        if "FUTURE" in text[m.start()-40:m.start()].upper():
            future.append(entry)
        else:
            daily.append(entry)
    return {"future": future, "daily": daily}

def format_task_line(t: dict) -> str:
    parts = [
        f"{t['status']}{t['priority']}",
        f"depends_on: {t['depends_on']}" if t['depends_on'] else None,
        f"task: {t['task']}",
        f"start: {t['start']}" if t['start'] else None,
        f"due: {t['due']}" if t['due'] else None,
        f"end: {t['end']}" if t['end'] else None,
        f"place: {t['place']}" if t['place'] else None,
        f"method: {t['method']}" if t['method'] else None,
        f"role: {t['role']}" if t['role'] else None,
        f"tags: {t['tags']}" if t['tags'] else None,
        f"id: {t['id']}"
    ]
    return " | ".join(p for p in parts if p)

def run(argv=None):
    if not (GOALS_FILE.exists() and ACTIVE_FILE.exists() and MANIFEST_FILE.exists()):
        print("[!] Один из файлов не найден.")
        sys.exit(1)

    manifest = parse_manifest(MANIFEST_FILE)
    goals = parse_goals_structure(GOALS_FILE.read_text(encoding="utf-8"))
    active_blocks = parse_active_tasks(ACTIVE_FILE.read_text(encoding="utf-8"))

    print("📘 USER INFO")
    for k in ['name', 'email', 'role', 'created']:
        if k in manifest:
            print(f"{k.title():<9}: {manifest[k]}")
    print()

    for goal in goals:
        print(f"🎯 GOAL: {goal['id']} — {goal['name']}")
        for project in goal["projects"]:
            print(f"\n  📁 PROJECT: {project['id']} — {project['name']}")
            for task in project["tasks"]:
                print(f"    {format_task_line(task)}")
        print()

    print("🔮 FUTURE TASKS")
    for t in active_blocks["future"]:
        print(f"{format_task_line(t)}")
    print()

    print("📌 DAILY TASKS")
    for t in active_blocks["daily"]:
        print(f"{format_task_line(t)}")
    print()

# Entry point
if __name__ == "__main__":
    run()
