## **CryptoProtos Todo DSL**

To install CPTD DSL CLI on any computer, run in the terminal: pip install cptd
After that, CPTD DSL CLI will be installed on your computer! (https://pypi.org/project/cptd/)

CPTD-DSL is a high-level domain-specific language (HLD-DSL) that implements the Structured Task Declaration Model (STDM) for activity and goal management. It is designed for declarative representation of goals, subgoals, and operational units (tasks, habits, events) using a human-machine readable (HMR) syntax.

The language follows the principle of Semantic Lightweight Markup with Operational Context (SLMOC) and employs an Extensible Annotated Markup Language (EAML), which makes it simultaneously:
– suitable for manual editing and version control (VCS-compatible),
– compatible with CLI shells and visual UI interfaces,
– optimized for offline use and automated analysis.

Thus, CPTD-DSL serves as a universal solution for text-based GTD, striking a balance between machine formalizability and human readability.

CPTD-DSL is not just a tool. It is a new generation thinking environment.
It is the language of those who do not go with the flow, but build their own destiny.
Those who replace chaos with a system, laziness with a priority, forgetfulness with order.

It is a method for those who decide not just to live, but to set goals, comprehend and win.
Every day you do not just keep a file - you shape yourself, layer by layer, line by line.

CPTD-DSL is a declaration of personal evolution.
And if you write, then you are in the game......

### **Official Documentation: CPTD System**

### **1. Brief Definition**

**CPTD (CryptoProtos Task Definition / Compact Planning & Tracking DSL)** — is a minimalistic, universal text-based DSL (Domain-Specific Language) designed for planning, tracking, and analyzing progress on goals, projects, and tasks.

It's a tool for those who want to clearly see what needs to be done, when, and why. It replaces dozens of applications with a single file that the user fully controls, ensuring **control, clarity, and sustained progress**.

### **2. Philosophy and Key Principles**

CPTD is built on a foundation that ensures user autonomy, reliability, and complete control.

* **Autonomy and Reliability:** The system is independent of the internet, clouds, and third-party services. Your data is solely yours.
* **Plain Text:** All data is stored in human-readable `.txt` or `.md` files. This guarantees longevity and accessibility.
* **Local-First:** Data is stored locally. The system works offline, in any text editor (Obsidian, VS Code, Notepad) on any platform.
* **VCS-Compatible:** The format is ideal for Version Control Systems (Git), allowing tracking of changes and collaborative work.
* **Manual Control:** No hidden magic. You fully control the process, ensuring maximum flexibility and awareness.
* **Simplicity and Depth:** The minimalistic syntax is easy to learn, yet it allows for describing complex projects and interdependencies.

### **3. What CPTD Allows You to Do: Key Features**

The system provides a full set of tools for structured task management.

* **🧠 Mentally Unload and Focus**
    * **Clear Decomposition:** Any goal is broken down into a `goal → project → task` hierarchy. This eliminates uncertainty and helps understand the next concrete step to take.
    * **Prioritization:** The `pri:A/B/C/D` attribute allows you to instantly differentiate important from secondary and focus your attention.
* **🎯 Achieve Goals Through Clear Steps**
    * **Progress Tracking:** The `progress:3/5` parameter visually shows movement towards the goal, which maintains motivation.
    * **Dependencies:** The ability to specify `depends:on:<id>` allows building logical chains of tasks where one action follows another.
* **🗂 Build a Dynamic and Scalable System**
    * **Daily Logs:** Maintaining daily files (`YYYYMMDD_cptd.md`) creates a rhythm and allows for storing a detailed work history.
    * **Archiving:** Completed goals and projects are moved to an archive, which clears the workspace and helps focus on what's current.
* **🧩 Flexibly Account for Everything Important**
    * **Roles and Assignees:** You can specify who is responsible for a task (`role:owner`, `role:other,Marina`).
    * **Categorization:** Tags (`@work`, `@study`) allow easy filtering and grouping of tasks.
    * **Different Activity Types:** The system supports not only tasks (`task`) but also recurring habits (`habit`) and logging events (`event`).
* **📈 Automate and Analyze**
    * **Machine Readability:** The structured format can be parsed by scripts (e.g., in Python) to create reports, dashboards, diagrams, and integrate with other systems (ETL, CI/CD).

### **4. Areas of Application**

CPTD is a universal tool applicable in any area of life and work.

| Area        | Examples of Use                                              |
| :---------- | :----------------------------------------------------------- |
| **Study** | Tracking progress on topics, word repetition, course completion. |
| **Work** | Project and sub-task control, client management, reporting.   |
| **Life** | Habit formation, health control, finances, home organization. |
| **Creativity** | Creating plans for a book, music album, website development.   |
| **Team** | Role distribution, building dependent actions, work coordination. |

### **5. Technical Specification: CPTD as a DSL**

**CPTD (CryptoProtos Todo DSL)** is a High-Level Domain-Specific Language (HLD-DSL) based on the principles of EAML, DLRE, and SLMOC. The format is optimized for SPTM, compatible with ML-CLI tools, supports MHRPS-style recording, easily integrates into VCS, and is oriented towards autonomous, machine-readable GTD environments.

#### **DSL Criteria and CPTD Compliance**

| DSL Criterion                   | Is CPTD Compliant? | Explanation                                                    |
| :------------------------------ | :----------------- | :------------------------------------------------------------- |
| 🔤 **Has its own syntax** | ✅ Yes             | `goals:`, `project:`, `task:`, `pri:`, `id:` etc. are keywords of the language. |
| 🧠 **Limited to a domain** | ✅ Yes             | Domain: planning tasks, goals, and progress tracking.          |
| 📘 **Is machine-readable** | ✅ Yes             | The language structure allows it to be parsed and interpreted for automation. |
| 👤 **Simplifies human work** | ✅ Yes             | The syntax is easy to read, quick to edit, and intuitive.      |
| 🔁 **Has conventions and structures** | ✅ Yes             | Date format, hierarchy, status system, roles, and dependencies. |

#### **Conceptual Stack Decryption**

| Abbreviation   | Decryption                                 | Comment                                                     |
| :------------- | :----------------------------------------- | :---------------------------------------------------------- |
| **HLD-DSL** | High-Level Domain-Specific Language        | Primary language type.                                      |
| **EAML** | Extensible Annotated Markup Language       | Format for annotated (attribute-based) records.             |
| **DLRE** | Dual-Layer Readable Encoding               | Readable by both humans and machines.                       |
| **SPTM** | Structured Plain-Text Management           | Management of structured `.md` files.                       |
| **ML-CLI** | Machine-Logic Compatible with Command-Line Interfaces | Suitable for processing and management from CLI.            |
| **MHRPS** | Minimal Human-Readable Planning Syntax     | Compact and concise syntax.                                 |
| **VCS-compatible** | Version Control System Compatible        | Easily versioned via Git and others.                        |
| **SLMOC** | Semantic Lightweight Markup with Operational Context | Semantic lightweight markup with operational meaning.       |

---

### **Conclusion**

CPTD is not just a to-do list. It is a **framework for self-organization and structured thinking** that disciplines, focuses, reduces anxiety, and frees from digital noise, making the user **faster, more precise, and more collected**.
