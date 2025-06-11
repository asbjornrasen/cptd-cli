import re
from importlib.resources import files
import cptd_tools

def run(argv):
    try:
        manifest_path = files(cptd_tools) / 'cptd_manifest.cptd'
        text = manifest_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("[!] Не удалось найти cptd_manifest.cptd внутри пакета.")
        return

    structure = []
    inside_structure = False
    pattern = re.compile(r'^\s*-\s*(.+/)\s*$')

    for line in text.splitlines():
        if line.strip().startswith("structure:"):
            inside_structure = True
            continue
        if inside_structure:
            if not line.strip().startswith("-"):
                break
            match = pattern.match(line)
            if match:
                structure.append(match.group(1).strip())

    if not structure:
        print("[!] Поле structure: не найдено или пусто.")
        return

    ignore_lines = [
        "# Auto-generated .cptdignore based on embedded cptd_manifest.cptd",
        "*",
        ""
    ] + [f"!{folder}" for folder in structure] + [
        "",
        "# System files",
        ".DS_Store",
        "*.log",
        "*.tmp",
        "*.bak",
        "__pycache__/",
    ]

    with open(".cptdignore", "w", encoding="utf-8") as f:
        f.write("\n".join(ignore_lines))

    print(f"✅ Сгенерирован .cptdignore с {len(structure)} включёнными папками.")
