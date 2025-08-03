import argparse
import subprocess
import platform
import urllib.request
import json
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "install",
    "description": "Installing commands from the CPTD repository",
    "usage": "cptd install <name> [--with-deps] [--allow-insecure] | uninstall <name>",
    "arguments": [
        {"name": "<name>", "required": True, "help": "Command name (eg: portscanner)"},
        {"name": "--with-deps", "required": False, "help": "Install dependencies (if any)"},
        {"name": "--allow-insecure", "required": False, "help": "Allow commands with dangerous code"},
        {"name": "--list", "required": False, "help": "Getting a list of available commands from the repository"},
    ],
    "examples": [
        "cptd install portscanner --with-deps",
        "cptd uninstall portscanner"
    ]
}

REPOS = {
    "windows": "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/windows",
    "linux":   "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/linux",
    "darwin":  "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/macos"
}

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    if not argv:
        print("[!] Please enter the command name or 'uninstall'")
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--i", "--install", dest="install_name", help="Install command")
    group.add_argument("--u", "--uninstall", dest="uninstall_name", help="Uninstall command")

    parser.add_argument("--with-deps", action="store_true")
    parser.add_argument("--allow-insecure", action="store_true")
    parser.add_argument("--list", action="store_true", help="Show a list of available commands from the repository")


    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    if args.install_name:
        name = args.install_name
        os_key = platform.system().lower()
        repo_url = REPOS.get(os_key)
        if not repo_url:
            print(f"[!] Unsupported OS: {os_key}")
            return
        url = f"{repo_url}/{name}.zip"
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


    if args.list:
        os_key = platform.system().lower()
        repo_url = REPOS.get(os_key)
        if not repo_url:
            print(f"[!] Unsupported OS: {os_key}")
            return
        list_url = f"{repo_url}/plugins.json"
        try:
            print(f"[•] Getting a list from: {list_url}")
            with urllib.request.urlopen(list_url) as response:
                data = json.load(response)
                print("📦 Available commands:")
                for item in data:
                    print(f"  - {item['name']:15} v{item['version']:7} — {item['description']}")
        except Exception as e:
            print(f"[!] Failed to load list: {e}")
        return
