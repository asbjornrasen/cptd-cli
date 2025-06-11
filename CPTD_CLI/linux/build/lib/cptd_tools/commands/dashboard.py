# cptd_tools/commands/dashboard.py

from __future__ import annotations

import argparse
import re
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict, Optional

# ──────────────────────────────────────────────────────────────────────────────
# Regex patterns (compiled once for performance)
# -----------------------------------------------------------------------------
GOAL_RE = re.compile(r"^####.*?goals:(?P<name>[^\n]+?) .*?id:(?P<gid>G\d+)(?: .*?progress:(?P<prog>\d+/\d+))?", re.MULTILINE)
PROJECT_RE = re.compile(r"^\t+[^\n]*?project:(?P<name>[^\n]+?) .*?id:(?P<pid>G\d+_P\d+)(?: .*?progress:(?P<prog>\d+/\d+))?", re.MULTILINE)
RE_DAILY_HEADER = re.compile(r"^\*+[- ]+DAILY[- ]+\*+$", re.IGNORECASE | re.MULTILINE)
RE_FUTURE_HEADER = re.compile(r"^\*+[- ]+FUTURE TASK[- ]+\*+$", re.IGNORECASE | re.MULTILINE)
RE_TASK_DAILY_HEADER = re.compile(r"^\*+[- ]+TASK DAILY[- ]+\*+$", re.IGNORECASE | re.MULTILINE)
HABIT_LINE_RE = re.compile(r"^\[[^\]]*\]habit:(?P<name>.+)")
DAILY_TASK_LINE_RE = re.compile(r"^\[[^\]]*\]\[[^\]]*\]\s*task:(?P<name>[^\n]+?)(?:\s|$)")
FUTURE_TASK_LINE_RE = re.compile(r"^(?:\*|\[).*?task:(?P<name>.+?)\s+goals:(?P<goal>[^\s]+)\s+project:(?P<project>[^\s]+).*?due:(?P<due>\d{4}-\d{2}-\d{2})", re.IGNORECASE)
DATE_IN_FILENAME_RE = re.compile(r"^(?P<date>\d{8})_cptd\.md$")
COMPLETED_BOX_RE = re.compile(r"^\s*\[[Xx]\]")

# ──────────────────────────────────────────────────────────────────────────────
# Helper functions
# -----------------------------------------------------------------------------

def get_base_path_from_config() -> Optional[Path]:
    config_file = Path.home() / ".cptd_config.json"
    if config_file.exists():
        with config_file.open(encoding="utf-8") as f:
            data = json.load(f)
        if "basepath" in data:
            return Path(data["basepath"])
    return None

def find_latest_daily_file(directory: Path) -> Path:
    dated_files: List[Tuple[datetime, Path]] = []
    for p in directory.glob("*_cptd.md"):
        m = DATE_IN_FILENAME_RE.match(p.name)
        if m:
            dt = datetime.strptime(m.group("date"), "%Y%m%d")
            dated_files.append((dt, p))
    if not dated_files:
        raise FileNotFoundError("No daily CPTD files (YYYYMMDD_cptd.md) found in directory")
    dated_files.sort(key=lambda t: t[0], reverse=True)
    return dated_files[0][1]

def parse_goals(goals_text: str) -> List[Tuple[str, str, Optional[str]]]:
    goals = []
    for m in GOAL_RE.finditer(goals_text):
        goals.append((m.group("gid"), m.group("name").strip(), m.group("prog")))
    return goals

def parse_projects(goals_text: str) -> List[Tuple[str, str, str, Optional[str]]]:
    projects = []
    for m in PROJECT_RE.finditer(goals_text):
        pid = m.group("pid")
        gid = pid.split("_P")[0]
        projects.append((gid, pid, m.group("name").strip(), m.group("prog")))
    return projects

def extract_section(content: str, header_re: re.Pattern, next_header_res: List[re.Pattern]) -> str:
    header_match = header_re.search(content)
    if not header_match:
        return ""
    start = header_match.end()
    end_positions = [m.start() for r in next_header_res for m in r.finditer(content, start)]
    end = min(end_positions) if end_positions else len(content)
    return content[start:end]

def parse_daily_file(daily_path: Path):
    with daily_path.open(encoding="utf-8") as f:
        text = f.read()
    daily_block = extract_section(text, RE_DAILY_HEADER, [RE_FUTURE_HEADER, RE_TASK_DAILY_HEADER])
    future_block = extract_section(text, RE_FUTURE_HEADER, [RE_TASK_DAILY_HEADER])
    task_daily_block = extract_section(text, RE_TASK_DAILY_HEADER, [])
    habits = [m.group("name").strip() for m in HABIT_LINE_RE.finditer(daily_block)]
    daily_tasks = [m.group("name").strip() for m in DAILY_TASK_LINE_RE.finditer(task_daily_block)]
    future_tasks = [(m.group("name").strip(), m.group("goal").strip(), m.group("project").strip(), m.group("due")) for m in FUTURE_TASK_LINE_RE.finditer(future_block)]
    return {"habits": habits, "daily_tasks": daily_tasks, "future_tasks": future_tasks, "raw": text}

def compute_stats(daily_raw: str) -> Dict[str, int]:
    total = len([l for l in daily_raw.splitlines() if l.strip().startswith("[*") or l.strip().startswith("[]") or l.strip().startswith("[X]")])
    completed = len([l for l in daily_raw.splitlines() if COMPLETED_BOX_RE.match(l)])
    overdue = 0
    active = total - completed
    planned = len(re.findall(r"^\\*", daily_raw, re.MULTILINE))
    return {"total": total, "completed": completed, "active": active, "overdue": overdue, "planned": planned}

# ──────────────────────────────────────────────────────────────────────────────
# CLI entry‑point
# -----------------------------------------------------------------------------

def dashboard_cmd(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Show CPTD dashboard (latest daily file + goals)")
    parser.add_argument("--dir", type=Path, help="Directory containing CPTD files (overrides config)")
    args = parser.parse_args(argv)

    directory = args.dir or get_base_path_from_config() or Path.cwd()
    goals_file = directory / "goals_cptd.md"
    if not goals_file.exists():
        sys.exit("goals_cptd.md not found in directory")

    try:
        latest_daily = find_latest_daily_file(directory)
    except FileNotFoundError as e:
        sys.exit(str(e))

    goals_text = goals_file.read_text(encoding="utf-8")
    goals = parse_goals(goals_text)
    projects = parse_projects(goals_text)
    daily_info = parse_daily_file(latest_daily)
    stats = compute_stats(daily_info["raw"])

    today_str = latest_daily.stem[:8]
    today_date = datetime.strptime(today_str, "%Y%m%d").date()

    print(f"\n📅 DASHBOARD — {today_date.isoformat()} (latest)\n")

    print("🎯 Goals [active]")
    if not goals:
        print("  (no goals found)\n")
    else:
        for gid, name, prog in goals:
            prog_disp = f"→ Progress: {prog}" if prog else ""
            print(f"- {gid:<5} {name:<20} {prog_disp}")
        print()

    print("📁 Projects")
    if not projects:
        print("  (no projects found)\n")
    else:
        for gid, pid, pname, prog in projects:
            prog_disp = f"→ Progress: {prog}" if prog else ""
            print(f"- {pid:<10} {pname:<20} {prog_disp}")
        print()

    print("🗓️  DAILY")
    if daily_info["habits"]:
        print(" Habits:")
        for h in daily_info["habits"]:
            print(f"   - {h}")
    if daily_info["daily_tasks"]:
        print(" Tasks:")
        for t in daily_info["daily_tasks"]:
            print(f"   - {t}")
    print()

    print("🔮 FUTURE TASKS")
    if not daily_info["future_tasks"]:
        print("  (none)\n")
    else:
        for name, goal, project, due in daily_info["future_tasks"]:
            print(f"- [ ] {name}  (goal:{goal} project:{project} due:{due})")
        print()

    print("📈 Stats:")
    print(f"- Total tasks:     {stats['total']}")
    print(f"- Completed:       {stats['completed']}")
    print(f"- Active:          {stats['active']}")
    print(f"- Overdue:         {stats['overdue']}")
    print(f"- Planned:         {stats['planned']}")
    print(f"\n🕒 Last update: {today_date.isoformat()}\n")

# Entry‑point for setuptools console_scripts
if __name__ == "__main__":
    dashboard_cmd()

# Required by CPTD CLI entry point mechanism
run = dashboard_cmd
