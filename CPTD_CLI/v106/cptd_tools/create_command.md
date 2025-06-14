
# 🧩 How to Add a New Command to the CPTD CLI

Thank you for your interest in developing a command for the **CPTD CLI**—a declarative system for managing goals, projects, and tasks. Below are the rules and templates you must follow when creating a command.




## ⚠️ Rules for Command Authors

### ❌ Do NOT include auto-installation of dependencies in your command code

You **must not** use logic that installs modules dynamically inside your Python scripts. This kind of code is **strictly forbidden** and will **fail validation**:

```python
try:
    import yaml
except ImportError:
    print("[\u2022] Missing dependency: pyyaml. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyyaml"], check=True)
    import yaml
```

Such code introduces hidden behavior, makes dependency tracking unreliable, and compromises security and reproducibility.

---

### ✅ Declare all dependencies in the manifest

Instead, **list all required packages** in the command’s manifest file:

```yaml
name: yourcommand
description: Description of your command
version: 1.0
entrypoint: yourcommand.py
dependencies:
  - pyyaml
author: Your Name
email: your@email.com
```

The CPTD CLI will automatically install the declared dependencies when the command is added using `--with-deps`.

---

This ensures a **clean**, **secure**, and **predictable** environment across all CPTD-based systems.

# 📦 `command` — Manage CLI Commands in CPTD CLI

The `cptd command` command allows you to **add** and **delete** custom CLI commands within the CPTD CLI system by directly interacting with the installed `cptd_tools/commands` directory.

---

## 🔹 Syntax

```bash
cptd command --add <path_to_file.py>
cptd command --del <filename.py>
```
---

## 📁 1. How to Create the Command File and Manifest Files

Generate a template and  automatically:

```bash
cptd newcommand --name yourcommand
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
# → add your command into CLI
cptd command --add yourcommand.py

# → should list your command
cptd list

# → prints help via SYNTAX
cptd yourcommand --help

# → executes the command
cptd yourcommand --input ./tasks.md --flag

```

If you need you may delete your command:

```bash
cptd command --del yourcommand.py
```

---

## 🛡 5. Standards

- `SYNTAX` is **mandatory**
    
- `run(argv)` is **mandatory**
    
- `--help` must not rely on `argparse`; use `print_help(SYNTAX)` instead
    
- Code must be clean, readable, and free of unnecessary dependencies
    

---


## 📄 6. Manifest Files Required for Each Command

📁 **All manifest files must be placed in the same directory as the command script.**  
For example, if your command is `yourcommand.py`, then both `manifest.yaml` and `manifest.json` must reside in the same folder.


Every command must be accompanied by **two manifest files** describing its metadata:

- `manifest.yaml` (YAML format)  
- `manifest.json` (JSON format)

Both files must contain the following fields:

| Field         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `name`        | Unique name of the command                                                  |
| `description` | Short explanation of what the command does                                  |
| `target`      | Operating system(s) supported: `linux`, `windows`, `macos`, or `all`        |
| `version`     | Semantic version (e.g., `1.0.0`)                                            |
| `entrypoint`  | Filename of the command script (e.g., `yourcommand.py`)                     |
| `dependencies`| List of Python packages the command depends on                              |
| `author`      | Name of the developer                                                       |
| `email`       | Contact email address                                                       |
| `github`      | Link to the developer’s GitHub profile or repository                        |
| `website`     | Developer’s personal or project website (optional)                          |
| `license`     | License filename or short identifier (e.g., `MIT`, `license.md`)            |


> 📌 **Important**:  
> The `target` field must explicitly declare which platforms the command supports.  
> Use `"all"` for cross-platform commands or list them as a comma-separated string (e.g., `"linux,windows"`).




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