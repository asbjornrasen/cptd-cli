from pathlib import Path
from datetime import date

def run(argv):
    target_dir = Path.cwd()
    today_str = date.today().strftime('%Y-%m-%d')
    daily_log_name = f"{today_str}_cptd.md"

    files_to_create = {
        "goals_cptd.md": "# Цели\n\n[][A]goals:Пример цели id:G001 status:activ progress:0/1\n",
        "archive_cptd.md": "# Архив целей\n\n[archive]\n",
        "user_manifest.cptd": f"""## User Manifest

version: 1.0.0
created: {today_str}
author: you@example.com

description: "Пользовательский манифест целей, задач и активности"
""",
        daily_log_name: f"# Ежедневный лог {today_str}\n\n[] task:Начать планирование дня\n"
    }

    print(f"📁 Инициализация проекта CPTD в: {target_dir.resolve()}\n")

    for filename, content in files_to_create.items():
        file_path = target_dir / filename
        if file_path.exists():
            print(f"⚠️  {filename} уже существует — пропущен")
        else:
            file_path.write_text(content, encoding="utf-8")
            print(f"✅ Создан файл: {filename}")

    print("\n🎉 Инициализация завершена. Теперь вы можете редактировать цели и задачи.")
