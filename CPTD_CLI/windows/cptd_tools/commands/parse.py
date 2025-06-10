import argparse
from pathlib import Path
import re

def run(argv):
    parser = argparse.ArgumentParser(description='Разбор CPTD-файла')
    parser.add_argument('filepath', type=Path, help='Путь к CPTD-файлу')
    args = parser.parse_args(argv)

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

