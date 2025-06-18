---

# 🧩 How to Add a New Command to CPTD CLI

Thank you for your interest in extending **CPTD CLI**.

---

## 📦 Submission Format (ZIP ONLY)

All CPTD CLI commands must be submitted as a **`.zip` archive**.

---

### ✅ Example of a Simple Command

```
📦 taskcleaner.zip
    ├── main.py
    ├── manifest.yaml
    └── manifest.json
```

---

### ✅ Example of a Project-Level Command with Subfolders

```
📦 taskmanager.zip
    ├── main.py
    ├── manifest.yaml
    ├── manifest.json
    ├── util/
    │   └── parser.py
    └── service/
        └── api.py
```

---

### ❗ Rules:

* `main.py`, `manifest.yaml`, and `manifest.json` must be located **at the root of the archive**

* The archive **must not contain a nested folder** named after the command

* The archive name determines the command name:
  `taskcleaner.zip` → `cptd taskcleaner`

* `manifest.yaml` and `manifest.json` must both explicitly define `entrypoint: main.py`

* If `main.py` is placed in a subfolder — ❌ the command will be rejected

* Both manifest files (YAML and JSON) are required

* Folders like `util/` and `service/` are allowed and encouraged for modular design

* Auto-installation of dependencies in code is strictly prohibited

---

## 📦 2. Mandatory Elements of a Command

Each command must contain the following **required elements**:

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

> This is the entry point invoked when the command is executed.

---

### ✅ 2.3 `--help` Handling and Help Output

```python
if "--help" in argv or "-h" in argv:
    print_help(SYNTAX)
    return
```

> Ensures unified help and autodocumentation support.

---

### ✅ 2.4 Use of `print_help(SYNTAX)` on Errors

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

## 🧪 4. Testing or Add Your Command

```bash
# → add your command into CLI
cptd command --add yourcommand.zip

# → should list your command
cptd list

# → prints help via SYNTAX
cptd yourcommand --help

# → Run your command
cptd yourcommand 
```


If you need you may delete your command:

```bash

cptd command --del yourcommand

```

---

## 🛡 5. Standards

* `SYNTAX` is **required**

* `run(argv)` is **required**

* `--help` must not rely on `argparse`; use `print_help(SYNTAX)` only

* Code must be clean, readable, and free from unnecessary dependencies

---

## 📄 6. Required Manifest Files

📁 **Both manifest files must be in the same folder as `main.py`**.

* `manifest.yaml` — for human readability

* `manifest.json` — for machine parsing

### Required fields in both manifests:

| Field          | Description                                           |
| -------------- | ----------------------------------------------------- |
| `name`         | Unique name of the command (matches the archive name) |
| `description`  | What the command does                                 |
| `version`      | Version (`1.0.0`)                                     |
| `entrypoint`   | Always `main.py`                                      |
| `target`       | Target OS (`all`, `linux`, `windows`, `macos`)        |
| `dependencies` | Required pip libraries                                |
| `author`       | Author's name                                         |
| `email`        | Contact email                                         |
| `github`       | GitHub link of author or project                      |
| `website`      | Website (optional)                                    |
| `license`      | License (`MIT`, `license.md`, etc.)                   |

---

## 🙌 Ready? Submit Your Command to the Official CPTD CLI Repository

1. Fork the repository:
   [https://github.com/asbjornrasen/cptdcli-plugin](https://github.com/asbjornrasen/cptdcli-plugin)

2. Create a branch:
   `feature/mycommand`

3. Add your ZIP archive to:
   `cptdcli-plugin/community_plugin/yourcommand.zip`

4. Make sure that:

   * structure is correct

   * `main.py`, manifests and folders are at the root of the archive

   * `--help` works

   * no auto-install logic is included

5. Append your plugin's manifest to the end of the community-plugins.json file in the required format. Replace `example` with your own metadata:

```json
{
  "name": "example",
  "description": "example",
  "version": "1.0.0",
  "target": "Windows",
  "entrypoint": "example.py",
  "dependencies": ["example"],
  "author": "example",
  "email": "example@example.com",
  "github": "https://github.com/example/example",
  "website": "https://example.com",
  "license": "example.md"
}
```

When specifying `"target"`, define the OS your plugin supports: `Windows`, `Linux`, `MacOS`, or `All`.

6. Submit a Pull Request with a description.

---

💡 Tip: Follow the philosophy of CPTD — **clarity**, **modularity**, **practicality**.

Need a template?

```bash
cptd newcommand
```

You’ll receive a complete two-project structure including `main.py`, `manifest.yaml`, `util/`, and `service/`.

---

Ready to create commands? CPTD CLI awaits your idea.
The best ones may be included in the official release.

---
Add Project into CPTD CLI
---
PS E:\> cptd

[ℹ] Usage: cptd <command> [args]
     Run `cptd list` to see all available commands.

PS E:\> cptd newcommand  

[debug] Looking for guide at: C:\Users\user44\AppData\Local\Programs\Python\Python313\Lib\site-packages\cptd_tools\create_command.md  
[✔] Created: Project_one/yourcommand, Project_two/yourcommand  

PS E:\> cptd list  

 Available commands:
  - ✅ about — Describe what this command does  
  - ✅ command — Describe what this command does  
  - ✅ dsl — Describe what this command does  
  - ✅ newcommand — Describe what this command does 
  
PS E:\> cptd command --add .\test01.zip 

[✓] Command 'test01' added.  
📄 Description: Demo CLI command with substructure  
🔰 Entrypoint : main.py  
👤 Author     : example  

[•] Dependencies listed: example  
[?] Install dependencies via pip? [Y/n]: y  
Requirement already satisfied: example in c:\users\user44\appdata\local\programs\python\python313\lib\site-packages (0.1.0)  

Requirement already satisfied: six in c:\users\user44\appdata\local\programs\python\python313\lib\site-packages (from example) (1.17.0)  
[✓] Dependencies installed.  

PS E:\> cptd list  

 Available commands:
  - ✅ about — Describe what this command does
  - ✅ command — Describe what this command does
  - ✅ dsl — Describe what this command does
  - ✅ newcommand — Describe what this command does
  - ✅ test01 — Demo CLI command with substructure  
  
PS E:\> cptd test01  
usage: cptd --input INPUT [--flag]  
cptd: error: the following arguments are required: --input   

PS E:\> cptd test01 --help  

 YOURCOMMAND — Demo structure with submodules  
  
Usage:
  cptd yourcommand --input <path> [--flag]

Arguments:
  --input         (required) - Path to the input file or folder
  --flag          (optional) - Optional flag

Examples:
  cptd yourcommand --input file.cptd
  cptd yourcommand --input folder --flag

PS E:\>