### **CPTD CLI**

**CPTD CLI** is not just a command-line tool. It is an extensible management platform designed for:  
• Creating custom commands and extensions;  
• Sharing commands between users;  
• Integrating with external tools and APIs;  
• Automating workflows, reporting, and strategic analysis;  
• Acting as the engine for any custom or graphical interface (UI).

---

### **Architecture Principles**

**1. CLI as an Extensible Platform**  
Each command is a standard Python file with a defined interface. You can create your own command in under 5 minutes.  
Commands are simple Python modules with minimal structure. Each command includes a manifest file containing information (name, description, author, version, dependencies). Developers can use the `cptd newcommand` template to get started quickly.

Commands can be tested and debugged interactively without restarting the system:

```bash
cptd command --add yourcommand.zip     # add command (ZIP only)  
cptd command --del yourcommand         # remove command  
```

Run the command:

```bash
cptd yourcommand
```

Run the project:

```bash
cptd yourcommand
```

---

**2. Security and Validation**  
• All commands in the public repository undergo strict security review.  
• Upon installation, automatic checks are performed for prohibited code (e.g., `pip install` inside the command).  
• When publishing to the public repository, each command is checked for security, structure, and manifest integrity.  
• Community-contributed commands are moderated before publication.

---

**3. CLI as the Engine for UI**  
The CLI acts as a bridge for graphical interfaces that use it as the backend. **CPTD CLI** serves as the backend for all current and future interfaces. All logic is processed through the CLI.

---

**4. Centralized and Decentralized Distribution**  
• Commands can be downloaded and used from the public repository.  
• A standard format for importing, exporting, and sharing commands is supported.

---

**5. Autonomy and Reliability**  
• Fully offline operation — no cloud required.  
• No telemetry, hidden data collection, or external connections.  
• Supported on Windows, Linux, and macOS.

---

### **Why This Matters**

• **Flexibility**: Adapt the CLI to any scenario — from license checking to automation.  
• **Scalability**: From individual developers to entire teams.  
• **Extensibility**: Creation, sharing, moderation, and integration of commands.  
• **Security**: Strict checks at all stages — install, execute, publish.  
• **Transparency**: All code is open, modular, and auditable.

---

### **Open Source and Repository**

CPTD CLI is a free open-source project [https://cptdcli.com](https://cptdcli.com)**   . 
The complete source code is available in the public repository:  
👉 **[https://github.com/asbjornrasen/cptd-cli](https://github.com/asbjornrasen/cptd-cli)**  
This ensures full transparency, builds trust and security, and allows anyone to verify, modify, or copy the system. Thanks to its openness, CPTD guarantees independence and verifiability in the long term.

## 🔹 List of Basic Commands for cptd

The following commands are available in the CPTD CLI:

| Command       | Purpose                                                                                   | Available |
|---------------|--------------------------------------------------------------------------------------------|-----------|
| `about`       | Shows information about CPTD CLI                                                           | yes       |
| `list`        | Displays all available commands                                                            | yes       |
| `dsl`         | Management of personal affairs through the declared DSL language, maintaining ToDo lists   | yes       |
| `newcommand`  | Generates a template for a new CLI command (for developers)                                | yes       |
| `command`     | Add, delete, or list custom CLI commands                                                   | yes       |
| `cpdsl`       | Interprets and executes `.dsl` registered CPTD CLI commands                                | yes       |
| `history`     | View, search, clear, or export the CPTD CLI command history                                | yes       |

> ⚠️ Note: The CLI is under active development and not yet ready for production use.

---

## 📥 How to Add a New Command to CPTD CLI

**Submission Format (ZIP only)**  
All CPTD CLI commands must be submitted as a `.zip` archive.

**Example of a Simple Command:**

```
taskcleaner.zip
├── main.py
├── icon.png
├── manifest.yaml
└── manifest.json
```

**Example of a Project Command with Subfolders:**

```
taskmanager.zip
├── main.py
├── icon.png
├── manifest.yaml
├── manifest.json
├── util/
│   └── parser.py
└── service/
    └── api.py
```

**Rules:**  
• `main.py`, `icon.png`, `manifest.yaml`, and `manifest.json` must be at the archive root  
• The archive must not contain a nested folder named after the command  
• Archive name defines the command name: `taskcleaner.zip` → `cptd taskcleaner`  
• In both manifests, the `entrypoint` field must be `main.py`  
• If `main.py` is not at the root — the command will be rejected  
• Both manifest files (YAML and JSON) are required  
• Subfolders like `util/`, `service/` are allowed  
• Auto-installing dependencies within the code is prohibited

---

### **Required Elements of a Command**

1. **Command Description in SYNTAX:**
    

```python
SYNTAX = {
  "name": "yourcommand",
  "description": "What the command does",
  "usage": "cptd yourcommand --input <path> [--flag]",
  "arguments": [
    {"name": "--input", "required": True, "help": "Path to input file"},
    {"name": "--flag", "required": False, "help": "Optional flag"}
  ],
  "examples": [
    "cptd yourcommand --input file.cptd",
    "cptd yourcommand --input folder --flag"
  ]
}
```

2. **`run(argv)` Function**
    

```python
def run(argv):
    ...
```

3. **Handle `--help`:**
    

```python
if "--help" in argv or "-h" in argv:
    print_help(SYNTAX)
    return
```

4. **Print help on error:**
    

```python
except Exception as e:
    print(f"[!] Argument error: {e}")
    print_help(SYNTAX)
    return
```

5. **Recommended Template:**
    

```python
from pathlib import Path
import argparse
from cptd_tools.syntax_utils import print_help

SYNTAX = {...}

def run(argv):
  if "--help" in argv or "-h" in argv:
    print_help(SYNTAX)
    return

  parser = argparse.ArgumentParser(...)
  parser.add_argument('--input', type=Path, required=True, ...)
  parser.add_argument('--flag', action='store_true', ...)

  try:
    args = parser.parse_args(argv)
  except Exception as e:
    print(f"[!] Argument error: {e}")
    print_help(SYNTAX)
    return

  if not args.input.exists():
    print(f"[!] Path does not exist:\n    {args.input}")
    return

  print(f"[✔] Processing: {args.input}")
  if args.flag:
    print("[✔] Flag is set")
```

---

### **Add or Test Command**

• Add: `cptd command --add yourcommand.zip`  
• View all: `cptd list`  
• Get help: `cptd yourcommand --help`  
• Run command: `cptd yourcommand`  
• Remove: `cptd command --del yourcommand`

---

### **Standards**

• `SYNTAX` is required  
• `run(argv)` is required  
• Use `print_help(SYNTAX)` only — do not rely on `argparse` for help  
• Code must be clean, readable, minimal dependencies

---

### **Manifests**

Manifests must be in the same folder as `main.py`:  
• `manifest.yaml` — human-readable  
• `manifest.json` — machine-readable

Required fields in the manifests:  
• `name`: unique name of the command (must match the archive name)  
• `description`: a description of the command  
• `version`: for example, 1.0.0  
• `entrypoint`: always `main.py`  
• `target`: supported operating systems (`all`, `linux`, `windows`, `macos`)  
• `dependencies`: list of required pip dependencies  
• `author`: name of the author  
• `email`: contact email  
• `github`: link to the GitHub repository  
• `website`: website (optional)  
• `license`: license (e.g., `MIT`, `license.md`, etc.)

---

## 🧩 `cpdsl` — Declarative Script Interpreter for CPTD

**Name:** `cpdsl`  
**Role:** Interpreter for `.dsl` scripts that sequentially execute installed `cptd` commands  
**Support:** Cross-platform (Linux / Windows / Mac)  
**Format:** YAML step definitions

---

### 🚀 What is `cpdsl` and Why Use It?

`cpdsl` is the official script interpreter of **CPTD CLI**. It executes YAML-defined commands line-by-line — turning manual sequences into structured, repeatable, and safe automation.

---

### 🧠 Why Use `cpdsl`?

• Automate routine processes with `cptd` commands  
• Replace fragile shell scripts with validated YAML instructions  
• Portability — one `.dsl` file can run anywhere  
• Transparent, repeatable, logged steps  
• Centralizes complex workflows: backup, encryption, upload, logging, etc.

---

### 📌 Why It's Convenient

• A single `.dsl` file defines a full workflow  
• Scenarios can be shared as modules  
• UI integration: e.g., "Run Backup" button  
• Debug and reuse scenarios easily

---

### 📊 Advantages of DSL Approach

|Feature|Advantage|
|---|---|
|📦 Unification|Uniform interface for all commands|
|♻️ Repeatability|One DSL can run on 1000 machines or schedule|
|📋 Self-documenting|DSL file reads like a technical spec|
|🧱 Extensibility|Easy to expand: if, loop, include, etc.|
|🔐 Security|No shell injection, no `eval`, no `rm -rf`|
|🧠 Cross-platform|One DSL works on Windows, Linux, servers|
|🧰 Integration|Use from UI, web panels, triggers, apps|

---

### 📂 Example Run

```bash
cptd cpdsl run backup.dsl --log out.txt --strict --wait-all --summary
```

---

### 📘 Official YAML Script Format

```yaml
name: "Script Name"
description: "Short purpose description"

steps:
  - name: "Step Name"
    command: "command_name"
    args:
      --flag1: value
      --flag2: true
    async: true
    depends_on: "step_name"
```

---

### 🧩 Field Descriptions

**Top-Level:**

|Field|Type|Purpose|
|---|---|---|
|`name`|string|Human-readable scenario name|
|`description`|string|Brief description|
|`steps`|list|List of step definitions|

**Inside `steps[]`:**

|Field|Type|Required|Description|
|---|---|---|---|
|`name`|string|No|Step name (for display or `depends_on`)|
|`command`|string|✅ Yes|Name of registered CPTD command|
|`args`|dict|No|Arguments — if value is `true`, flag is passed|
|`async`|bool|No|Run step in background if true|
|`depends_on`|string/list|No|Dependencies; run only after these steps|

**Environment Variables:**

```yaml
args:
  --password-env: SFTP_PASS
```

→ Becomes: `--password-env <value from SFTP_PASS>`

---

### ✅ Example Scenario (.dsl)

```yaml
name: "Backup"
description: "Mount, archive and upload data"

steps:
  - name: "Mount"
    command: "cpdisk"
    args:
      --mount: true
      --file: "vault.hc"

  - name: "Archive"
    command: "compress"
    args:
      --input: "/vault/data"
      --output: "/tmp/data.zip"
    depends_on: "Mount"

  - name: "Upload"
    command: "uploader"
    args:
      --file: "/tmp/data.zip"
      --target: "sftp://host/upload"
      --password-env: SFTP_PASS
    async: true
    depends_on: "Archive"
```

---

### 🧪 Run the Scenario

```bash
cptd cpdsl run backup.dsl --log log.txt --strict --wait-all --summary
```

**Arguments:**

|Argument|Meaning|
|---|---|
|`--log`|Save log to file|
|`--strict`|Stop on first error|
|`--wait-all`|Wait for all async steps to complete|
|`--summary`|Print table with statuses at the end|

**Sample Summary Table:**

```
Summary:
✔ Step 1 - Mount                [OK]
✔ Step 2 - Archive              [OK]
✔ Step 3 - Upload               [ASYNC]
```

---

### ⚠️ Error Handling

|Situation|Default|With `--strict`|
|---|---|---|
|`depends_on` points to missing step|Error|Error|
|Step exits with non-zero code|Continues|Stops|
|Async step fails|Warns|Stops|

---

### 🚀 Writing Tips

• Always provide unique `name:` for each step  
• Use `depends_on` to define logical sequence  
• Use `async: true` for background tasks  
• Store `.dsl` files in `scripts/` or `scenarios/` folders

---

### 🏁 Conclusion

**`cpdsl` is not just syntax. It's structure. It's automation strategy.**  
Forget the chaos of `bash` chains and `&&`.  
Create readable, repeatable, testable scenarios that evolve with your project.

---

### Ready? Submit Your Command to CPTD CLI

1. Fork: [https://github.com/asbjornrasen/cptdcli-plugin](https://github.com/asbjornrasen/cptdcli-plugin)
    
2. Create branch: `feature/mycommand`
    
3. Add ZIP: `community_plugin/yourcommand.zip`
    
4. Make sure:
    
    - Structure is valid
        
    - `main.py`, manifests at root
        
    - `--help` works
        
    - No auto-installation logic
        
5. Add manifest to `community-plugins.json`:
    

```json
{
  "name": "example",
  "description": "example",
  "long_description": "example",
  "version": "1.0.0",
  "target": "Windows",
  "entrypoint": "example.py",
  "dependencies": ["example"],
  "author": "example",
  "email": "example@example.com",
  "github": "https://github.com/example/example",
  "website": "https://example.com",
  "license": "example.md",
  "documentation":""
}
```

6. Submit Pull Request with description
    

---

**Tip:** Follow CPTD philosophy — clarity, modularity, practicality.

Need a template?

```bash
cptd newcommand
```

You'll get a project structure with `main.py`, `manifest.yaml`, `util/`, `service/`.

---

**Ready to create commands? CPTD CLI awaits your ideas.**  
The best ones will be included in the official release.

---

**Summary:**  
**CPTD CLI** is more than a tool. It’s a foundation for creating, testing, and sharing smart utilities.  
Its flexible architecture, strict security, and open model make it an ideal management core for both personal and enterprise systems.