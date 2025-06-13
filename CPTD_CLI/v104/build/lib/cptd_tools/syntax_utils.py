# cptd_tools/syntax_utils.py

def print_help(syntax: dict):
    print(f"\n {syntax.get('name', '').upper()} — {syntax.get('description', '')}\n")
    print("Usage:")
    print(f"  {syntax.get('usage', 'No usage info')}\n")

    args = syntax.get("arguments", [])
    if args:
        print("Arguments:")
        for arg in args:
            name = arg.get("name", "")
            required = "(required)" if arg.get("required", False) else "(optional)"
            help_text = arg.get("help", "")
            print(f"  {name:<15} {required:<10} - {help_text}")
        print()

    examples = syntax.get("examples", [])
    if examples:
        print("Examples:")
        for ex in examples:
            print(f"  {ex}")
    print()

def parse_args(argv: list[str], syntax: dict) -> dict:
    result = {}
    required_args = [a for a in syntax.get("arguments", []) if a.get("required", False)]
    expected_args = [a["name"] for a in syntax.get("arguments", [])]

    if len(argv) < len(required_args):
        print("[!] Missing required arguments.")
        print_help(syntax)
        exit(1)

    for i, expected in enumerate(expected_args):
        if i < len(argv):
            result[expected] = argv[i]
        else:
            result[expected] = None

    return result
