import argparse
from pathlib import Path
import re
from collections import Counter

def run(argv):
    parser = argparse.ArgumentParser(description='Генерация отчета по задачам')
    parser.add_argument('filepath', type=Path, help='Путь к CPTD-файлу')
    args = parser.parse_args(argv)

    pattern = re.compile(r"^(\[.\])\s+\[(.)\]\s+(task|project|goals):([^\n]+?)\s+(.*)$")

    counters = Counter()
    with open(args.filepath, encoding='utf-8') as f:
        for line in f:
            if match := pattern.match(line.strip()):
                status = match.group(1)
                counters[status] += 1

    print("\n--- Отчёт по статусам ---")
    for status, count in counters.items():
        label = {
            '[X]': 'Выполнено',
            '[]': 'Активно',
            '[-]': 'На паузе',
            '[!]': 'Остановлено'
        }.get(status, status)
        print(f"{label:12} : {count}")

    print(f"Всего записей : {sum(counters.values())}\n")