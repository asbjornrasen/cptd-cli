# hello.py

SYNTAX = {
    "name": "hello",
    "description": "A simple test command that says hello",
    "usage": "cptd hello [--name <username>]",
    "arguments": [
        {
            "name": "--name",
            "required": False,
            "help": "Optional name to greet"
        }
    ],
    "examples": [
        "cptd hello",
        "cptd hello --name Asbjorn"
    ]
}

def run(argv):
    import argparse

    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("--name", help="Your name", default="World")
    args = parser.parse_args(argv)

    print(f"👋 Hello, {args.name}!")
