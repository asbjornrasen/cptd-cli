from pathlib import Path
from datetime import date

def run(argv):
    target_dir = Path.cwd()
    today_str = date.today().strftime('%Y-%m-%d')
    daily_log_name = f"{today_str}_cptd.md"

    files_to_create = {
        "goals_cptd.md": "# Goals\n\n[][A]goals:Example of a goal id:G001 status:activ progress:0/1\n",
        "archive_cptd.md": "# Goals Archive\n\n[archive]\n",
        "user_manifest.cptd": f"""## User Manifest

version: 1.0.0
created: {today_str}
author: you@example.com

description: "User Manifestation of Goals, Tasks and Activities"
""",
        daily_log_name: f"# Daily log {today_str}\n\n[][] task:Start planning your day\n"
    }

    print(f"📁 Initializing the CPTD project in: {target_dir.resolve()}\n")

    for filename, content in files_to_create.items():
        file_path = target_dir / filename
        if file_path.exists():
            print(f"⚠️  {filename} already exists - skipped")
        else:
            file_path.write_text(content, encoding="utf-8")
            print(f"✅ File created: {filename}")

    print("\n🎉 Initialization is complete. You can now edit goals and tasks.")
