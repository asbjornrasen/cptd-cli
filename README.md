CryptoProtos Todo DSL and CPTD CLI
To install CPTD DSL CLI on any computer, run in the terminal: pip install cptd
After that, CPTD DSL CLI will be installed on your computer! ([https://pypi.org/project/cptd/](https://pypi.org/project/cptd/))

🔧 What is CPTD CLI?
CPTD CLI is a flexible command-line system and the primary tool for automating, extending, and managing the functions of the entire system.

It allows you to:

* manage tasks, events, and DSL files,
* create your own commands and extensions,
* integrate commands with external tools (scripts, APIs, Git, CI/CD),
* share commands between users,
* run commands both from a local directory and from centralized repositories.

🧠 CPTD CLI is not just an interface, but a full-fledged operational shell
It serves as a bridge between:

* **CPTD DSL** — a structured text format for defining goals, projects, tasks, and events;
* **User interfaces** (current and future) — graphical environments that use the CLI as an engine;
* **User and system commands** — extensible automation modules within the ecosystem;
* **External tools and scripts** — through launching, exporting, analysis, reporting, and automation.

📦 It is not just a way to execute a command in the terminal — it is a universal control layer through which the user and the system exchange data, actions, and logic.
The CLI allows you not just to run code, but to orchestrate thinking, structure, and execution, combining DSL, visual UI, and operational logic into a single architecture.

🧩 Why CPTD CLI is important and unique
✅ 1. Flexibility and extensibility
Each command is a regular Python file with a defined interface.

You can create your own command in 5 minutes.

Automatic dependency installation is supported: the command declares what it needs.

Commands are distributed with their manifest: **name**, **description**, **author**, **version**, etc.

All commands in the common repository undergo strict security auditing.

✅ 2. Centralized and decentralized modes
You can use local commands (`./commands/`) or connect to a shared repository where users exchange scripts and utilities.

The system supports a standard format of distributed CLI command repositories.

✅ 3. Capabilities for administrators and users
Administrators can write commands that:

* analyze user activity,
* generate reports and strategic plans,
* check licenses and enforce security policies.

Users can automate repetitive actions, create templates, schedule workflows, and document their activity.

✅ 4. Minimalism + power
The CLI remains lightweight and intuitive: everything is stored in plain files.

No internet, heavy installations, or cloud services are required.

Works equally well on Windows, Linux, and macOS.

Fully works offline, secure, and suitable for controlled environments.

🛠 A core that can be extended without limits
The following commands are available in the initial CPTD CLI package:

| Command    | Purpose                                                    | Available |
| ---------- | ---------------------------------------------------------- | --------- |
| about      | Shows information about CPTD CLI                           | yes       |
| list       | Displays all available commands                            | yes       |
| dsl        | Manages CPTD DSL definitions                               | yes       |
| newcommand | Generates a template of a new CLI command (for developers) | yes       |
| command    | Adds, removes, or lists user commands (--add, --del)       | yes       |

🚀 Why you should use CPTD CLI
**Control:** Full access to your structure, data, and command logic — without third‑party dependencies.

**Security:** No tracking, no external data exchange — everything is local. Ideal for internal, protected, or classified environments.

**Scalability:** Works from a single user up to a team of 100+ people without changing the architecture.

**Compatibility:** Works with Git, integrates with Python, supports CI/CD.

**Ecosystem growth:** Connect hundreds of unique commands, share them, and build a unified DSL‑oriented ecosystem.

🔁 CPTD CLI as a platform for extension and exchange
CPTD CLI is not just a management tool, but a development platform designed for sharing, customization, and functional expansion through user commands.

🔨 Create your own commands
CPTD CLI commands are regular Python modules with minimal structure.

Any user can create a command in 1–2 minutes using the `cptd newcommand` template.

You will immediately be provided with templates for development and all the necessary instructions for reactive development of new projects and commands.

Commands are described by a manifest: **name**, **version**, **author**, **description**, **dependencies**.

🌐 Share and connect
Commands can be distributed, shared, and loaded from common repositories.

A modular plugin‑like design is used, similar to Obsidian or Homebrew.

Loading from the network, GitHub, or local storage is supported — with centralized connection for team work.

⚙️ Automatic dependency handling
On the first run, a command can automatically install the necessary dependencies from its manifest.

The user does not need to manually configure the environment — the system will do everything itself.

📌 Why this matters
**Flexibility:** Adapt the CLI to any workflow — from license checks to automatic reports.

**Scalability:** Individual users or teams can expand functionality independently.

**Community power:** Create and share a growing library of commands and solutions.

**Autonomy:** Everything works locally, transparently, and without hidden mechanisms.

🚀 CPTD DSL CLI — this is not just TODO. It is an ecosystem.
CPTD DSL CLI is more than a task management tool.
It is part of the powerful CryptoProtos ecosystem, connecting goal tracking, secure data storage, planning, automation, and encryption into a single modular structure.

🔹 Write. Structure. Encrypt. Control. Expand the core by adding commands from the available repository on the site.
🔹 Use the full power of CryptoProtos — from licensing to synchronization.
🔹 Add your own commands — the CLI supports dynamic expansion. Create modules and connect them with a single line.
🔹 Safely delete or replace commands — the flexible architecture adapts to your workflow.

💡 CPTD DSL CLI is your personal interface for managing reality.
You are not just making a to‑do list — you are designing your own system of thinking and action.

📦 **Installation:**

```
pip install cptd
```

🎯 **Initialize CPTD in the working directory (optional):**

```
cptd dsl --init
```

🛠 **Create a command template for developing your own command:**

```
cptd newcommand
```

📦 **Add a user command:**

```
cptd command --add myscript.zip
```

📦 **Remove a command:**

```
cptd command --del myscript
```

🎯 **Run a user command:**

```
cptd myscript
```

Now you can extend and customize CPTD CLI to fit your workflows.

**CPTD DSL CLI — think like a developer. Live like an architect.**
CryptoProtos — Security. Modules. Control.

🔄 Share commands. Expand CPTD DSL CLI together.
CPTD DSL CLI is not only your personal system —
it is an open ecosystem in which you can create and share commands with others.

💡 **Want to share your automation, parser, generator, or utility?**
Now it is as simple as ever:

📤 **How to share a command:**
Write a command using the established template: `mycommand.zip`

Send the file to a friend, colleague, or team — or publish it.

Done!

📥 **How to install someone else’s command? Just 3 steps:**
1️⃣  Get the file `mycommand.py`
2️⃣  `pip install cptd`
3️⃣  `cptd command --add myscript.zip`

💥 Done! Now the command can be run from anywhere:

```
cptd mycommand
```

🎯 Expand the CLI as you need.
🧠 Share ideas. Get tools from others.
⚙️ CPTD CLI — Modules. Flexibility. Community.

CPTD CLI is not just a terminal. It is an extensible command system with which users can create, automate, and share truly working tools.

---

**What is CPTD‑DSL?**
*(Initialization: `cptd dsl --init`)*

CPTD‑DSL is a high‑level domain‑specific language (HLD‑DSL) that implements the Structured Task Description Model (STDM) for managing activities and goals. It is intended for declarative representation of goals, sub‑goals, and operational units (tasks, habits, events) using syntax convenient for both humans and machines (HMR).

The language follows the principle of Semantic Lightweight Markup with Operational Context (SLMOC) and uses the Extensible Annotated Markup Language (EAML), which makes it simultaneously:
– suitable for manual editing and version control (compatible with VCS),
– compatible with CLI shells and visual interfaces,
– optimized for offline work and automated analysis.

Thus, CPTD‑DSL is a universal text‑based GTD solution that finds the balance between machine‑formalizability and human readability.

CPTD‑DSL is not just a tool. It is a next‑generation thinking environment.
It is the language of those who do not drift with the current, but build their own destiny;
those who replace chaos with a system, laziness with priority, forgetfulness with order.

It is a method for those who have decided not just to live, but to set goals, understand, and win.
Every day you save not just a file — you shape yourself, layer by layer, line by line.

**CPTD‑DSL is a declaration of personal evolution.**
And if you are writing, then you are already in the game…

---

### Official documentation: CPTD system

#### 1. Brief definition

CPTD (CryptoProtos Task Definition / Compact Planning & Tracking DSL) is a minimalist universal text DSL designed for planning, tracking, and analyzing progress toward goals, projects, and tasks.

It is a tool for those who want to clearly see what needs to be done, when, and why. It replaces dozens of applications with a single file that the user fully controls, providing control, clarity, and sustainable progress.

#### 2. Philosophy and key principles

CPTD is built on a foundation that ensures **autonomy, reliability, and full user control**.

* **Autonomy and reliability:** The system does not depend on the internet, clouds, and third‑party services. Your data belongs only to you.
* **Plain text:** All data is stored in human‑readable `.txt` or `.md` files. This guarantees longevity and accessibility.
* **Local‑First:** Data is stored locally. The system works offline in any text editor (Obsidian, VS Code, Notepad) on any platform.
* **VCS compatibility:** The format is ideal for version control systems (Git), allowing tracking changes and collaborative work.
* **Manual control:** No hidden magic. You fully control the process, ensuring maximum flexibility and awareness.
* **Simplicity and depth:** The minimalist syntax is easy to learn, but it allows describing complex projects and interdependencies.

#### 3. What CPTD enables: key features

The system provides a full set of tools for structured task management.

🧠 **Unload your brain and focus**

* **Clear decomposition:** Any goal is broken down into the hierarchy `goal → project → task`. This eliminates uncertainty and helps understand the next specific step.
* **Prioritization:** The `pri:A/B/C/D` attribute allows you to instantly distinguish the important from the secondary and focus attention.

🎯 **Achieve goals through clear steps**

* **Progress tracking:** The `progress:3/5` parameter clearly shows the movement toward a goal, supporting motivation.
* **Dependencies:** The ability to specify `depends:on:<id>` allows building logical chains of tasks where one action follows another.

🗂 **Build a dynamic and scalable system**

* **Journals:** Keeping daily files (`YYYYMMDD_cptd.md`) creates a rhythm and allows storing a detailed work history.
* **Archiving:** Completed goals and projects are moved to the archive, which cleans up the workspace and helps focus on the current.

🧩 **Flexibly account for everything important**

* **Roles and performers:** You can specify who is responsible for a task (`role:owner`, `role:other`,Marina).
* **Categorization:** Tags (`@work`, `@study`) allow easily filtering and grouping tasks.
* **Different types of activity:** The system supports not only tasks (`task`), but also regular habits (`habit`) and event logging (`event`).

📈 **Automate and analyze**

* **Machine readability:** The structured format can be parsed by scripts (e.g., in Python) to create reports, dashboards, diagrams, and integrate with other systems (ETL, CI/CD).

#### 4. Areas of application

CPTD is a universal tool applicable in any sphere of life and work.

| Area       | Examples of use                                                   |
| ---------- | ----------------------------------------------------------------- |
| Study      | Tracking progress on topics, word repetition, course completion.  |
| Work       | Project and sub‑task control, client management, reporting.       |
| Life       | Habit formation, health control, finances, home organization.     |
| Creativity | Planning a book, music album, website development.                |
| Team       | Role distribution, building dependent actions, work coordination. |

#### 5. Technical characteristics: CPTD as a DSL

CPTD (CryptoProtos Todo DSL) is a high‑level DSL based on the principles of **EAML, DLRE, and SLMOC**. The format is optimized for **SPTM**, compatible with **ML‑CLI**, supports the **MHRPS** writing style, is easily integrated into **VCS**, and is oriented toward autonomous GTD environments readable by machines.

| DSL criteria                      | Does CPTD comply? | Explanation                                                         |
| --------------------------------- | ----------------- | ------------------------------------------------------------------- |
| 🔤 Own syntax                     | ✅ Yes             | Keywords `goals:`, `project:`, `task:`, `pri:`, `id:`, etc.         |
| 🧠 Domain‑restricted              | ✅ Yes             | Domain: task planning, goals, and progress tracking.                |
| 📘 Machine‑readable               | ✅ Yes             | The structure allows parsing the language and automating processes. |
| 👤 Simplifies human work          | ✅ Yes             | Syntax is easy to read, quickly edit, and intuitive.                |
| 🔁 Has conventions and structures | ✅ Yes             | Date format, hierarchy, status system, roles, and dependencies.     |

**Decoding the conceptual stack**

| Abbreviation   | Decoding                                             | Comment                                               |
| -------------- | ---------------------------------------------------- | ----------------------------------------------------- |
| HLD‑DSL        | High-Level Domain-Specific Language                  | Type of language.                                     |
| EAML           | Extensible Annotated Markup Language                 | Format of annotated records.                          |
| DLRE           | Dual-Layer Readable Encoding                         | Readable for humans and machines.                     |
| SPTM           | Structured Plain-Text Management                     | Management of structured .md files.                   |
| ML‑CLI         | Machine‑Logic Compatible with CLI                    | Suitable for processing from CLI.                     |
| MHRPS          | Minimal Human‑Readable Planning Syntax               | Compact, succinct syntax.                             |
| VCS‑compatible | Compatible with version control systems              | Easy to version via Git etc.                          |
| SLMOC          | Semantic Lightweight Markup with Operational Context | Semantic lightweight markup with operational meaning. |

---

### Conclusion

CPTD is not just a to‑do list. It is a framework for self‑organization and structural thinking that disciplines, focuses, reduces anxiety, and frees you from digital noise, making you faster, more accurate, and more collected.

CryptoProtos CPTD — design your thinking. Share tools.
**One language. Unlimited possibilities.**
