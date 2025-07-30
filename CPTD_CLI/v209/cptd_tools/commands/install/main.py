import argparse
import subprocess
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "install",
    "description": "Установка или удаление команд из репозитория CPTD",
    "usage": "cptd install <name> [--with-deps] [--allow-insecure] | uninstall <name>",
    "arguments": [
        {"name": "<name>", "required": True, "help": "Имя команды (например: portscanner)"},
        {"name": "--with-deps", "required": False, "help": "Установить зависимости (если есть)"},
        {"name": "--allow-insecure", "required": False, "help": "Разрешить команды с опасным кодом"},
    ],
    "examples": [
        "cptd install portscanner --with-deps",
        "cptd uninstall portscanner"
    ]
}

REPO_URL = "https://www.cptdcli.com/repo01"

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    if not argv:
        print("[!] Укажите имя команды или 'uninstall'")
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--i", "--install", dest="install_name", help="Установить команду")
    group.add_argument("--u", "--uninstall", dest="uninstall_name", help="Удалить команду")

    parser.add_argument("--with-deps", action="store_true")
    parser.add_argument("--allow-insecure", action="store_true")

    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    if args.install_name:
        name = args.install_name
        url = f"{REPO_URL}/{name}.zip"
        cmd = ["cptd", "command", "--add", url]
        if args.with_deps:
            cmd.append("--with-deps")
        if args.allow_insecure:
            cmd.append("--allow-insecure")
        print(f"[→] Installing from {url}...")
        subprocess.run(cmd)

    if args.uninstall_name:
        name = args.uninstall_name
        cmd = ["cptd", "command", "--del", name]
        print(f"[→] Removing command '{name}'...")
        subprocess.run(cmd)
