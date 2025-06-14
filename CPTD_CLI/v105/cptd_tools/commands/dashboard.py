from __future__ import annotations
import re, sys
from pathlib import Path
from typing import List, Dict, OrderedDict

GOALS_FILE    = Path("goals_cptd.md")
ACTIVE_FILE   = Path("active_cptd.md")
MANIFEST_FILE = Path("user_manifest.cptd")

# ────────────────────── универсальный парсер поля ──────────────────────
FIELD_RE = re.compile(r"(\w+):\s*([^:\n]+?)(?=\s+\w+:|$)", re.IGNORECASE)
STATUS_RE = re.compile(r"^\s*(\[[^\]]*\]\s*\[[^\]]*\])")

def fields_dict(line: str) -> Dict[str, str]:
    return {k.lower(): v.strip() for k, v in FIELD_RE.findall(line)}

# ───────────────────────── парсинг manifest ────────────────────────────
def parse_manifest(path: Path) -> Dict[str, str]:
    if not path.exists():
        return {}
    return {k.strip().lower(): v.strip()
            for k, v in (l.split(':', 1)
                         for l in path.read_text(encoding="utf-8").splitlines()
                         if ':' in l)}

# ────────────────────── парсинг структуры целей ────────────────────────
def parse_goals_structure(text: str):
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

# ────────────────────── активные задачи ────────────────────────────────
def parse_active_tasks(text: str):
    future, daily = [], []
    for m in re.finditer(r".*task:.*", text, re.IGNORECASE):
        raw = m.group(0)
        f   = fields_dict(raw)
        block = future if "FUTURE" in text[max(0, m.start()-80):m.start()].upper() else daily
        block.append({"raw": raw, "fields": f})
    return {"future": future, "daily": daily}

# ─────────────────────────── форматирование ────────────────────────────
FIELD_ORDER = ['depends_on', 'task', 'start', 'due', 'end',
               'place', 'method', 'role', 'tags', 'id']

def fmt_task(raw: str, fields: Dict[str, str], indent: int = 0) -> str:
    prefix = ""
    m = STATUS_RE.match(raw)
    if m:
        prefix = m.group(1).strip() + " "
    ordered = []
    for key in FIELD_ORDER:
        if key in fields:
            ordered.append(f"{key}: {fields[key]}")
    # добавим любые новые поля, которые пользователь может ввести
    for k, v in fields.items():
        if k not in FIELD_ORDER:
            ordered.append(f"{k}: {v}")
    return " " * indent + prefix + " | ".join(ordered)

# ────────────────────────────── main ───────────────────────────────────
def run(argv=None):
    for p in (GOALS_FILE, ACTIVE_FILE, MANIFEST_FILE):
        if not p.exists():
            sys.exit(f"[!] file not found: {p}")

    manifest = parse_manifest(MANIFEST_FILE)
    goals    = parse_goals_structure(GOALS_FILE.read_text(encoding="utf-8"))
    active   = parse_active_tasks   (ACTIVE_FILE.read_text(encoding="utf-8"))

    # ---------- USER INFO ----------
    print("📘 USER INFO")
    print(f"Name     : {manifest.get('name', '')}")
    print(f"Email    : {manifest.get('email', '')}")
    print(f"Role     : {manifest.get('role', '')}")
    print(f"Created  : {manifest.get('created', '')}\n")

    # ---------- GOALS / PROJECTS / TASKS ----------
    for g in goals:
        gid   = g['fields'].get('id', '')
        gname = g['fields'].get('goals', '')
        print(f"🎯 GOAL: {gid} — {gname}\n")
        for p in g['projects']:
            pid   = p['fields'].get('id', '')
            pname = p['fields'].get('project', '')
            print(f"  📁 PROJECT: {pid} — {pname}")
            for t in p['tasks']:
                print(fmt_task(t['raw'], t['fields'], indent=4))
            print()

    # ---------- FUTURE / DAILY ----------
    print("🔮 FUTURE TASKS")
    for t in active["future"]:
        print(fmt_task(t['raw'], t['fields']))
    print()

    print("📌 DAILY TASKS")
    for t in active["daily"]:
        print(fmt_task(t['raw'], t['fields']))
    print()

if __name__ == "__main__":
    run()
