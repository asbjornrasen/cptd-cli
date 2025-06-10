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
        import_path = f'cptd_tools.commands.{args.command}'
        # print(f'[debug] Импорт модуля: {import_path}')
        module = importlib.import_module(import_path)
        # print(f'[debug] Модуль загружен: {module}')
        module.run(unknown)
    except Exception as e:
        print(f'\n[!] Ошибка при выполнении команды: {args.command}')
        print(f'[trace] {type(e).__name__}: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()