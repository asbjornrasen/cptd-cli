
# 🧩 How to Add a New Command to the CPTD DSL CLI

Thank you for your interest in developing a command for the **CPTD DSL CLI**—a declarative system for managing goals, projects, and tasks. Below are the rules and templates you must follow when creating a command.

---

## 📁 1. Where to Create the Command File

Create a new Python file **anywhere in your working copy of the project** (note: the `commands/` directory is the **required** location for commands in the distribution; from there they are automatically installed and registered).  
Alternatively, generate a template automatically:

```bash
cptd newcommand --name yourcommand
```

📄 Example:

```
commands/mycommand.py
```

---

## 📦 2. Mandatory Elements of a Command

Each command must contain the following **required blocks**:

### ✅ 2.1 `SYNTAX` — Command Description

```python
SYNTAX = {
    "name": "yourcommand",
    "description": "What this command does.",
    "usage": "cptd yourcommand --input <path> [--flag]",
    "arguments": [
        {"name": "--input",
         "required": True,
         "help": "Path to input file"},
        {"name": "--flag",
         "required": False,
         "help": "Optional flag"}
    ],
    "examples": [
        "cptd yourcommand --input file.cptd",
        "cptd yourcommand --input folder --flag"
    ]
}
```

---

### ✅ 2.2 `run(argv)` Function

```python
def run(argv):
    ...
```

> This is the entry point invoked by `main.py`.

---

### ✅ 2.3 `--help` Handling and Help Output

```python
if "--help" in argv or "-h" in argv:
    print_help(SYNTAX)
    return
```

> Ensures unified help and autodocumentation support.

---

### ✅ 2.4 Use `print_help(SYNTAX)` on Errors

```python
except Exception as e:
    print(f"[!] Argument error: {e}")
    print_help(SYNTAX)
    return
```

---

## 🧩 3. Recommended Template

```python
from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "yourcommand",
    "description": "Describe what this command does.",
    "usage": "cptd yourcommand --input <path> [--flag]",
    "arguments": [
        {"name": "--input", "required": True, "help": "Path to the input file or folder"},
        {"name": "--flag", "required": False, "help": "Optional flag to control behavior"}
    ],
    "examples": [
        "cptd yourcommand --input file.cptd",
        "cptd yourcommand --input folder --flag"
    ]
}

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser(description=SYNTAX["description"], add_help=False)
    parser.add_argument('--input', type=Path, required=True, help='Path to the input file or folder')
    parser.add_argument('--flag', action='store_true', help='Optional flag')

    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    if not args.input.exists():
        print(f"[!] Input path does not exist:\n    {args.input}")
        return

    print(f"[✔] Processing input: {args.input}")
    if args.flag:
        print("[✔] Flag is set.")
```

---

## 🧪 4. Testing Your Command

```bash
cptd help
# → should list your command

cptd yourcommand --help
# → prints help via SYNTAX

cptd yourcommand --input ./tasks.md --flag
# → executes the command
```

---

## 🛡 5. Standards

- `SYNTAX` is **mandatory**
    
- `run(argv)` is **mandatory**
    
- `--help` must not rely on `argparse`; use `print_help(SYNTAX)` instead
    
- Code must be clean, readable, and free of unnecessary dependencies
    

---

## 🙌 Ready? 🛠️ How to Propose a New Command for CPTD DSL CLI release

To have your command included in the **official CPTD DSL CLI release**, please follow these steps:

---

### ✅ Contribution Guide

1. **Fork** the repository:  
    [CPTD-DSL on GitHub](https://github.com/asbjornrasen/cptd-dsl)
    
2. **Create a new branch** named after your command, for example:  
    `feature/mycommand`
    
3. **Add your command file** to the following directory:  
    `CPTD_CLI/cptd_tools/commands/`
    
4. Make sure your command:
    
    - follows the style of the project,
        
    - provides a help option (`--help`),
        
    - does not break the existing CLI structure.
        
5. **Open a Pull Request** with a brief description of your command and its purpose.
    
6. After review and approval, your command will be included in the **official release**.
    

---

💡 _Tip: Follow the philosophy of the tool — clarity, modularity, and practical utility for daily task management._

Need help with a command template or code review? Feel free to ask.

Thank you for contributing to the CPTD DSL CLI!