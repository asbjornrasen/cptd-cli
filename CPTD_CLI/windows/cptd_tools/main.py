import argparse
import importlib
import sys
import pkgutil
import cptd_tools.commands  # используется для help

def list_available_commands():
    return [name for _, name, _ in pkgutil.iter_modules(cptd_tools.commands.__path__)]

def main():
    parser = argparse.ArgumentParser(prog='cptd', description='CPTD CLI Tool')
    parser.add_argument('command', help='Команда (parse, report, help, ...)')
    args, unknown = parser.parse_known_args()

    if args.command == 'help':
        print("\n Доступные команды:")
        for name in list_available_commands():
            print(f"  - {name}")
        print("\nПример: cptd report goals_cptd.md")
        return

    try:
        module = importlib.import_module(f'cptd_tool.commands.{args.command}')
        module.run(unknown)
    except ModuleNotFoundError:
        print(f'\n[!] Неизвестная команда: {args.command}')
        sys.exit(1)

if __name__ == '__main__':
    main()