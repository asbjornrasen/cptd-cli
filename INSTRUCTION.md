
---

## Guide to Using the CPTD System

CPTD is a text-based system for managing goals, projects, and tasks. It helps you structure your plans, track progress, and maintain daily logs in simple `.md` files.

### 1. File Structure

It is recommended to store all files in a single folder, organized by year.

```
📁 2025/
├── goals_cptd.md         ← general structure: goals, projects, tasks
├── archive_cptd.md       ← archive of all completed goals
├── dictionary_cpdt.md    ← dictionary of all terms and parameters
├── 2025-06-01.cptd.md    ← daily log file
├── 2025-06-02.cptd.md    ← ...
└── ...
```

### 2. The Main File: `goals_cptd.md`

This file is your control panel. Here, you describe all major goals and break them down into projects and specific tasks.

**Structure:**

- **goals:** — A global objective (e.g., for a quarter or year).
- **project:** — A part of a goal, a major block of work.
- **task:** — A specific action that needs to be performed.

**Example:**

Markdown

```
### [][A] goals:health id:G001 status:active progress:2/4

    [][A] project:nutrition id:G001_P01 progress:2/2
        [X][A] task:eliminate sugar id:G001_P01_T01
        [X][B] task:drink 2L of water per day id:G001_P01_T02
    [][B] project:sleep id:G001_P02 progress:0/2
        [][C] task:go to bed before 23:00 id:G001_P02_T01
        [][B] task:don't use phone after 22:00 id:G001_P02_T02

### [][B] goals:work id:G002 status:active progress:1/3
    [][A] project:reports id:G002_P01 progress:0/1
        [][] task:write May report id:G002_P01_T01
    [][B] project:clients id:G002_P02 progress:1/1
        [X][B] task:call new client id:G002_P02_T01
    [][A] project:accounting id:G002_P03 progress:0/2
        [][A] task:request tax form id:G002_P03_T01 role:other,Marina
        [][C] task:attach form to report id:G002_P03_T02 depends:on:<G002_P03_T01>
```

### 3. Daily Files: `YYYYMMDD_cptd.md`

Each day, you create a new file in the `YYYYMMDD_cptd.md` format where you log the tasks for the day.

**Working with Tasks:**

- **If a task is not completed**, it is moved to the next day. In the old file, it is marked as `[*]`, and an active copy `[]` is created in the new file.

**Example of `20250601_cptd.md` file:**

Markdown

```
----- DAILY -----
progress:4/9
[]habit:Brush teeth
[]habit:Drink at least 1.5 liters of water
[X]habit:Take vitamins
[X]habit:Walk the dog
[]habit:Study each target language for 1 hour
[X]habit:Read news for 20 minutes
[X]habit:Exercise for 20 minutes
[]habit:Eye exercises
[]habit:Tidy up for 15 minutes

-------FUTURE TASK--------------
[*][A] start:2025-07-14 task:create backup server goals:192.150.0.120 project:server due:2025-07-16

[*][A] start:2025-06-20 task:add new license goals:cryptoprotos project:cryptoprotosK method:server due:2025-06-25

--------TASK DAILY--------------

[X] [A] task:eliminate sugar start:2025-06-01 end:2025-06-01 due:2025-06-01 id:G001_P01_T01
[X] [B] task:call new client start:2025-06-01 due:2025-06-01 id:G002_P02_T01
[X] [C] task:learn 20 words start:2025-06-01 due:2025-06-01 method:quizlet id:G003_P01_T01
[]  [B] task:write May report start:2025-06-02 due:2025-06-02 id:G002_P01_T01
[]  [A] task:go to bed before 23:00 start:2025-06-03 due:2025-06-03 id:G001_P02_T01

```

### 4. Archiving: `archive_cptd.md`

When a goal is fully achieved (all its projects and tasks are completed), it is moved from `goals_cptd.md` to `archive_cptd.md`. When archiving, the goal, projects, and tasks are removed from the main `goals_cptd.md` file.

**Archive Example:**

Markdown

```
### [X][A] goals:health start:2025-06-03 due:2025-06-06 progress:4/4 id:G001

    [X][A] project:nutrition start:2025-06-03 due:2025-06-04 progress:2/2 id:G001_P01
        [X][A] task:eliminate sugar id:G001_P01_T01
        [X][B] task:drink 2L of water per day id:G001_P01_T02
    [X][] project:sleep start:2025-06-03 due:2025-06-06 progress:2/2 id:G001_P02
        [X][B] task:go to bed before 23:00 id:G001_P02_T01
        [X][C] task:don't use phone after 22:00 id:G001_P02_T02
```

### 5. CPTD Dictionary of Terms

This section describes all the special words and symbols used in the system.

[] — Task is active, not yet completed

[X] — Task completed

[-] — Task is on pause

[!] — Task is stopped or canceled

goals: — Main goal — a major result (for a month, quarter, year).

project: — Sub-goal or block within a goal.

task: — A specific action that needs to be performed.

habit: — A recurring behavior (daily, weekly, etc.).

`[]A/B/C/D` — **Task priority:**

- `A` — urgent
- `B` — important
- `C` — desirable
- `D` — optional

id:G001_P01_T01 — Unique identifier. Do not change an ID after it has been created to avoid breaking links.

progress:3/5 — Progress: 3 of 5 units completed.

start:YYYYMMDD — Task start date.

due:YYYYMMDD — Task deadline.

depends:on:<id> — Indicates a dependency on another task.

role:other,<name> — The task is performed by another person.

method:anki — Method or tool for completion.

tags:focus,urgent — Tags for filtering and sorting.

### 6. Recommendations for Maintaining Files

- **Structure:** Store all `.cptd.md` files in a separate directory, organized by year or project.
- **Identifiers (ID):** Use the `Gxxx_Pxx_Txx` structure. Do not change an ID after its creation.
- **Working with Tasks:** Do not delete tasks, even canceled ones—mark them with `[!]`.
- **Progress:** Manually update the `progress:x/y` field in `goals_cptd.md` when the status of tasks changes.
- **Syntax:** Maintain a consistent order of parameters (`status priority start_date task id deadline...`) for readability.
- **Dates:** Always use the `YYYYMMDD` format.
