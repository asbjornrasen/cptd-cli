# cptd_tools/commands/init.py

from pathlib import Path
from datetime import datetime

def run(argv):
    target_dir = Path.cwd()
    today_str = datetime.today().strftime('%Y-%m-%d')

    files_to_create = {
        "goals_cptd.md": (
            "# Goals\n\n"
            "[][A]goals:Example of a goal id:G001 progress:0/1\n"
            "   [][A]project:Example of a goal id:G001_P01 progress:0/1\n"
            "       [][A]task:Example of a goal id:G001_P01_T01 \n"
        ),
        "archive_cptd.md": (
            "# Goals Archive\n\n"
            
        ),
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

    print(f"\n📁 Initializing the CPTD project in: {target_dir.resolve()}\n")

    for filename, content in files_to_create.items():
        file_path = target_dir / filename
        if file_path.exists():
            print(f"⚠️  {filename} already exists - skipped")
        else:
            file_path.write_text(content, encoding="utf-8")
            print(f"✅ File created: {filename}")

    print("\n🎉 CPTD initialization complete. Ready to plan your goals.")
