# parser.py
import argparse
from pathlib import Path
import re
import json  # нужно для конфигурационного файла

def run(argv):
    parser = argparse.ArgumentParser(description='Разбор CPTD-файла')
    parser.add_argument('filepath', type=Path, help='Путь к CPTD-файлу')
    args = parser.parse_args(argv)

    args.filepath = resolve_path(args.filepath)

    pattern = re.compile(
        r"^\s*\[(.?)\]\[(.?)\]\s*(task|project|goals):\s*([^\n]+?)\s*(.*)$",
        re.IGNORECASE
    )

    with open(args.filepath, encoding='utf-8') as f:
        for line in f:
            if match := pattern.match(line.strip()):
                status, priority, typ, name, rest = match.groups()
                print(f"{typ.upper()} | {status} : {priority} | {name.strip()}{rest.strip()}")
                # print(f"{typ.upper():7} | [{s1}][{s2}] {name.strip():<40} {rest.strip()}")
                # print(f"{typ.upper():7} | [{s1}][{s2}] {name.strip():<40} :: {rest.strip()}")

def resolve_path(filepath: Path) -> Path:
    if filepath.exists():
        return filepath
    config = Path.home() / '.cptd_config.json'
    if config.exists():
        with open(config, encoding='utf-8') as f:
            base = json.load(f).get('base_path')
            full_path = Path(base) / filepath
            if full_path.exists():
                return full_path
    return filepath  # пусть упадёт естественно
