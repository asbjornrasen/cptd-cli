#main.py

import argparse
import importlib
import sys
import pkgutil
import cptd_tools.commands  

def list_available_commands():
    return [name for _, name, _ in pkgutil.iter_modules(cptd_tools.commands.__path__)]

def main():
    if len(sys.argv) == 1:
        print("\n[ℹ] Usage: cptd <command> [args]")
        print("     Run `cptd help` to see all available commands.")
        return

    parser = argparse.ArgumentParser(prog='cptd', description='CPTD CLI Tool', add_help=False)
    parser.add_argument('command', help='commands (parse, report, help, ...)')
    args, unknown = parser.parse_known_args()

    if args.command == 'help':
        print("\n Available commands:")
        for name in list_available_commands():
            print(f"  - {name}")
        print("\nExample: cptd report goals_cptd.md")
        return

    try:
        import_path = f'cptd_tools.commands.{args.command}'
        module = importlib.import_module(import_path)
        module.run(unknown)
    except ModuleNotFoundError:
        print(f"[!] Unknown command: {args.command}")
        print("    Use `cptd help` to list available commands.")
    except Exception as e:
        print(f"\n[!] Error executing command: {args.command}")
        print(f'[trace] {type(e).__name__}: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
