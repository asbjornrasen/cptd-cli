# 🔧 What is CPTD-DSL CLI?

**CPTD-DSL CLI** is a command-line utility for working with `.cptd.md` or `.txt` files written in the **CPTD-DSL** format (Structured Goal & Task Language).

It provides a structured interface for managing your goals, projects, tasks, habits, and daily entries directly from the terminal.

---

## ✨ Key Features

- 📂 **Parse and inspect** structured goals, projects, tasks, habits, and events  
- 🔍 **Filter and query** by type, priority, status, progress, or date  
- 📊 **Generate statistics**: completed vs active tasks, progress summaries per goal or project  
- ⚙️ **Integrate with automation** tools like Git, Cron, Makefile, or CI pipelines  
- 🔁 **Export data** to `JSON`, `HTML`, or `SVG` for visualization or further processing

---

## 🚀 Example Commands

```bash
cptd parse 20250611_cptd.md
````

> Outputs a structured view of all tasks, projects, and goals with priorities and status markers.

```bash
cptd stats --goal=G001
```

> Displays a progress summary of the goal `G001`, including active/completed tasks and current progress.

```bash
cptd export --format=json
```

> Converts the CPTD-DSL file into a machine-readable JSON format.

---

## 🧠 Philosophy

CPTD-DSL CLI is not just a tool — it’s a **thinking interface**.
It empowers you to treat your goals and projects as **structured data**, enabling deeper reflection, precision, and automation.

> **Structure your thoughts. Track your progress. Own your trajectory.**

---

## 📁 Supported File Format

* `.cptd.md` — Markdown-compatible CPTD-DSL files
* `.txt` — Plain text files using CPTD-DSL syntax

All files remain **human-readable**, **Git-friendly**, and **offline-compatible**.

## **📦 Community Contributions Welcome: Add Your Command to CPTD CLI or propose Your Commands**

🛠️ Developers are welcome to propose new commands for inclusion in the CPTD DSL CLI.
If you have an idea that fits the philosophy of the tool, feel free to open an issue or submit a pull request.

Best regards, CryptoProtos team.

---

**CPTD-DSL CLI** — *because structured thinking deserves a structured interface.*

```
```
