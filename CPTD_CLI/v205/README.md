CPTD CLI provides the user with a powerful and flexible platform for project management, task automation, and functionality extension through user-defined commands. Here are the main advantages and practical benefits:

Practical benefits for the user

1. Automation and task optimization
   The user can create commands and programs tailored to their needs: data collection, log analysis, file transformation, cache cleanup, system updates, launching complex projects and individual software modules — all of this becomes a single CLI command.
   Example:
   Instead of complex Bash or PowerShell scripts, one can write a modular command in Python and quickly call it via cptd mytool.
   Also, for example, you wrote a project for news parsing and result sorting — and you need to:

* run it regularly with a single click without opening the terminal;
* see a shortcut on the desktop with a clear icon;
* share this tool with colleagues or clients as an "application".
  You can package the project into a ZIP as the newsparser command, and then:

cptd command --add newsparser.zip
cptd installapp --add newsparser --icon news.png

Now:
With a single mouse click, the parser starts, connects to sources, filters by date or keywords, and outputs a ready list of articles to a file or terminal.
The user does not see the inner workings of the project: everything works like a ready-made application — you chose the name, icon, and launch behavior.
This makes CPTD CLI a powerful bridge between script development and the creation of full-fledged utilities that are convenient to use and distribute without building a separate .exe or .deb.

2. Rapid integration of custom solutions
   Thanks to ZIP plugin support and a simple structure, the user can easily adapt scripts into CLI commands and share them without needing to build a full application.

3. Reliability and protection
   Built-in OS verification (ensure\_compatible) prevents commands from being run on unsupported systems, eliminating execution errors and increasing stability.

4. A platform for collaboration
   The system supports a unified command standard and centralized repository — meaning commands can be distributed via GitHub and used within a team or organization.
   Example:
   Developers and DevOps engineers can exchange ready-made commands and connect them with a single action.

5. Development without unnecessary dependencies
   The structure requirements and prohibition on auto-installing dependencies ensure code predictability and cleanliness. This is especially important in corporate or secure environments.

6. Universal framework for console utilities
   If the user often creates scripts, CPTD CLI eliminates the need to write separate wrappers — just package the script into a ZIP with a manifest.

7. Learning and skill development
   Working with CPTD CLI develops skills in Python, CLI application architecture, module writing, YAML/JSON usage, and teaches working in a standardized environment.
   In short:
   CPTD CLI is like npm or pip, but for your own system commands. It is your personal automation and command solution arsenal in a single manageable container.

8. Creating custom shortcuts for launching projects
   With the installapp command, the user can:
   Create desktop shortcuts for any custom command
   Set up their own launch system — as a GUI alternative to the command line
   Launch projects of any complexity (CLI utilities, Python programs, automated pipelines) with a single click from the familiar interface of Windows, Linux, or macOS
   Assign custom icons and shortcut names, adapting the appearance to personal preferences
   Example:
   You created the CLI command reportgen, which generates an analytical report from a database. With:

cptd installapp --add reportgen --icon analytics.png

...you get a full desktop shortcut that launches the report generation as a native application.

9. A core for user interfaces and external programs
   CPTD CLI can act as a core or backend for graphical interfaces, web applications, and other programs. Your projects can directly call CPTD commands, passing arguments and processing the result.
   What this provides:
   Moving application logic into a modular CLI command
   Using one core as the main mechanism for multiple interfaces
   Calling via subprocess, os.system, HTTP requests, or IPC
   Separating logic from presentation — the interface can be changed without rewriting the core
   Example:
   You are writing a graphical interface program for parsing and analyzing data. Instead of reimplementing business logic, the interface simply calls:

cptd datacleaner --input dataset.csv --remove-outliers

This ensures code reuse, ease of debugging, and faster development.

Conclusion:
CPTD CLI is not just a console. It is a structured command core that can serve as the foundation for GUI, REST API, automated pipelines, and enterprise solutions. It connects scripts and interfaces into a unified, scalable architecture.
CPTD CLI becomes not only a development tool, but also a platform for creating cross-platform applications with a familiar launch system. This is especially useful for system administrators, developers, data engineers, and anyone who wants to combine the power of the console with the convenience of a graphical interface.



CPTD CLI

CPTD CLI is not just a command-line tool.
It is an extensible management platform designed to:

- Create custom commands and extensions
- Enable command exchange between users
- Integrate with external tools and APIs
- Automate workflows, reporting, and strategic analysis
- Serve as the core engine for any user or graphical interfaces (UI)

Architectural Principles

1. CLI as an Extensible Platform

Every command is just a regular Python file with a defined interface.
You can create your own command in under 5 minutes.

Commands are simple Python modules with minimal structure.
Each command includes a manifest file (name, description, author, version, dependencies).
Developers can use the "cptd newcommand" template to get started instantly.

Commands can be tested and debugged interactively during development using:
  
cptd command --add yourcommand.zip (adds the command to the CLI system - only ZIP)
  
cptd command --del yourcommand  (removes the command)  

This enables rapid prototyping, testing, and cleanup without restarting or rebuilding the system.

Run your command:  

cptd yourcommand  

Run your project:  

cptd yourcommand  

2. Security and Validation  

All commands in the shared repository undergo strict security review.
During installation, CPTD CLI performs automatic checks for forbidden code (e.g., dynamic pip install inside command files).
During publishing to the shared repository, each command undergoes rigorous validation for security, structure, and manifest integrity.
When submitted by the community, commands are moderated and reviewed before inclusion in the official repository.

3. CLI as a Core Engine for UI

It serves as a bridge between graphical environments that use CLI as their core engine.
CPTD CLI acts as the core backend for all present and future interfaces.
All UI components interact with the CLI for logic processing and data operations.

4. Centralized and Decentralized Distribution

Commands can be shared and loaded from shared repositories.
Follows a standardized format for sharing, importing, and distributing CLI commands.

5. Autonomy and Reliability

Works fully offline — no cloud required.
No telemetry, no hidden data collection, no external connections.
Compatible with Windows, Linux, and macOS.

Why It Matters

Flexibility: Adapt CLI to any workflow — from license checks to automation.
Scalability: From solo developers to enterprise teams.
Extensibility: Build, share, moderate, and integrate custom commands.
Security: Strict validation at all stages — installation, execution, and repository submission.
Transparency: All code is open, modular, and auditable.

6. Open Source and Public Repository

CPTD CLI is a free and open-source project.
Its full source code is available in the public repository:  
https://github.com/asbjornrasen/cptd-dsl

This guarantees full transparency, increases trust and security, and allows anyone to inspect, contribute to, or fork the system.
By being open, CPTD ensures long-term independence and verifiability.

Ready? Submit Your Command to the Official CPTD CLI Repository:

- Fork the repository:  
    [https://github.com/asbjornrasen/cptdcli-plugin](https://github.com/asbjornrasen/cptdcli-plugin)
    
- Create a branch:  
    feature/mycommand
    
- Add your ZIP archive to:  
    cptdcli-plugin/community_plugin/yourcommand.zip
    
- Ensure that:
    
    - the structure is correct
        
    - `main.py`, manifests, and folders are in the root of the archive
        
    - `--help` works
        
    - no auto-install logic is used
        
- Append your plugin manifest at the end of the `community-plugins.json` file with the following format:
    

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

When specifying "target", define the target OS: Windows, Linux, MacOS, or All.

---

Sure. Here's the same content in plain English text, with all Markdown formatting removed and nothing deleted:

---

How to Add a New Command to CPTD CLI
---

To add your command to the CLI, run:

cptd command --add yourcommand.zip

Submission Format (ZIP ONLY)

All CPTD CLI commands must be submitted as a `.zip` archive.

Example of a Simple Command:  

taskcleaner.zip  
├── main.py  
├── manifest.yaml  
└── manifest.json  

Example of a Project-Level Command with Subfolders:  

taskmanager.zip  
├── main.py  
├── manifest.yaml  
├── manifest.json  
├── util/  
│   └── parser.py  
└── service/  
└── api.py  

Rules:

* `main.py`, `manifest.yaml`, and `manifest.json` must be located at the root of the archive
* The archive must not contain a nested folder named after the command
* The archive name determines the command name:
  For example: `taskcleaner.zip` → `cptd taskcleaner`
* `manifest.yaml` and `manifest.json` must both explicitly define `entrypoint: main.py`
* If `main.py` is placed in a subfolder, the command will be rejected
* Both manifest files (YAML and JSON) are required
* Folders like `util/` and `service/` are allowed and encouraged for modular design
* Auto-installation of dependencies in code is strictly prohibited

Mandatory Elements of a Command

Each command must contain the following required elements:

1. `SYNTAX` — Command Description:  
  
SYNTAX = {  
"name": "yourcommand",  
"description": "What this command does.",  
"usage": "cptd yourcommand --input <path> \[--flag]",  
"arguments": \[  
{"name": "--input",  
"required": True,  
"help": "Path to input file"},  
{"name": "--flag",  
"required": False,  
"help": "Optional flag"}  
],  
"examples": \[  
"cptd yourcommand --input file.cptd",  
"cptd yourcommand --input folder --flag"  
]  
}  

2. `run(argv)` Function:  

def run(argv):
...

This is the entry point invoked when the command is executed.

3. `--help` Handling and Help Output:

if "--help" in argv or "-h" in argv:  
print\_help(SYNTAX)  
return  

This ensures unified help and autodocumentation support.

4. Use of `print_help(SYNTAX)` on Errors:  

except Exception as e:  
print(f"\[!] Argument error: {e}")  
print\_help(SYNTAX)  
return  

Recommended Template:  

from pathlib import Path  
import argparse  
from cptd\_tools.syntax\_utils import print\_help  

SYNTAX = {  
"name": "yourcommand",  
"description": "Describe what this command does.",  
"usage": "cptd yourcommand --input <path> \[--flag]",  
"arguments": \[
{"name": "--input", "required": True, "help": "Path to the input file or folder"},  
{"name": "--flag", "required": False, "help": "Optional flag to control behavior"}  
],  
"examples": \[  
"cptd yourcommand --input file.cptd",  
"cptd yourcommand --input folder --flag"  
]  
}  

def run(argv):  
if "--help" in argv or "-h" in argv:  
print\_help(SYNTAX)  
return  

---
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

---

What to add to every command:
---

At the very beginning of your `yourcommand.py` file, before any other imports, add:


from cptd_tools.os_guard import ensure_compatible
ensure_compatible(__file__)


What this call does:

* It reads the `manifest.yaml` or `manifest.json` file located next to the command file.
* It checks the `target` field.
* If the current operating system does not match the `target` value:

  * It prints a message,  
  * Deletes the command folder,  
  * Exits the execution using `sys.exit(1)`.  

Example beginning of a command:    


from cptd_tools.os_guard import ensure_compatible
ensure_compatible(__file__)  # ← this line is mandatory

from colorama import Fore  
from cptd_tools.syntax_utils import print_help  


Why this is important:

Even though `command --add` already filters commands by operating system, calling `ensure_compatible(__file__)`:

* Guarantees protection on every run, even if the command was manually added to the CLI.
* Automatically removes the command at runtime if the system is not compatible.
* Makes each command self-contained and secure.


---

Testing or Add Your Command:
---

To add your command to the CLI, run:

cptd command --add yourcommand.zip

To list all available commands:

cptd list

To view help for your command:

cptd yourcommand --help

To run your command:

cptd yourcommand

To delete your command:

cptd command --del yourcommand

---

Standards:

* `SYNTAX` is required
* `run(argv)` is required
* `--help` must not use `argparse`; use `print_help(SYNTAX)` only
* Code must be clean, readable, and free from unnecessary dependencies

Required Manifest Files:

Both manifest files must be in the same folder as `main.py`.

* `manifest.yaml` — human-readable
* `manifest.json` — machine-readable

Required fields in both manifests:  

name: Unique name of the command (must match the archive name)  
description: What the command does  
version: Version (example: 1.0.0)  
entrypoint: Always set to main.py  
target: Supported OS (example: all, linux, windows, macos)  
dependencies: Required pip libraries  
author: Author’s name  
email: Contact email  
github: GitHub link  
website: Website (optional)  
license: License (example: MIT, license.md, etc.)  

---

Ready? Submit Your Command to the Official CPTD CLI Repository:
---

1. Fork the repository:  
   [https://github.com/asbjornrasen/cptdcli-plugin](https://github.com/asbjornrasen/cptdcli-plugin)

2. Create a branch:
   feature/mycommand

3. Add your ZIP archive to:  
   cptdcli-plugin/community_plugin/yourcommand.zip

4. Ensure that:

   * the structure is correct
   * `main.py`, manifests, and folders are in the root of the archive
   * `--help` works
   * no auto-install logic is used

5. Append your plugin manifest at the end of the `community-plugins.json` file with the following format:

{  
"name": "example",  
"description": "example",  
"version": "1.0.0",  
"target": "Windows",  
"entrypoint": "example.py",  
"dependencies": \["example"],  
"author": "example",  
"email": "example@example.com",  
"github": "https://github.com/example/example",  
"website": "https://example.com",  
"license": "example.md"  
}  

When specifying "target", define the target OS: Windows, Linux, MacOS, or All.

1. Submit a Pull Request with a description.

Tip: Follow the CPTD philosophy — clarity, modularity, practicality.

Need a template?

cptd newcommand

You’ll get a ready-made project structure with `main.py`, `manifest.yaml`, `util/`, and `service/`.

Ready to build commands? CPTD CLI awaits your ideas.
The best ones may be included in the official release.


Summary

CPTD CLI is more than a tool — it is a foundation for building, validating, and exchanging smart operational utilities.
Its flexible architecture, strict security, and transparent model make it the ideal control core for personal and enterprise-level systems.


