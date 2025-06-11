import argparse
import json
from pathlib import Path

CONFIG_PATH = Path.home() / '.cptd_config.json'

def run(argv):
    parser = argparse.ArgumentParser(description='Сохранить базовый путь к CPTD-файлам')
    parser.add_argument('base_path', type=Path, help='Папка с CPTD-файлами')
    args = parser.parse_args(argv)

    if not args.base_path.exists():
        print("[!] Указанный путь не существует.")
        return

    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump({"base_path": str(args.base_path)}, f)

    print(f"[✔] Базовый путь сохранён: {args.base_path}")
