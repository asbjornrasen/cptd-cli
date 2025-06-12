
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

---
For a task in the CPTD system, the general format is as follows:

```

[status][priority] depends_on:<TaskID> task:Task Name start:YYYYMMDD end:YYYYMMDD due:YYYYMMDD  place:Location method:Tool role:role,name tags:tag1,tag2 id:UniqueID

```

| Element            | Meaning                                                               |
| ------------------ | --------------------------------------------------------------------- |
| `depends_on:`      | ID of another task that this task depends on                          |
| `[status]`         | Task status:                                                          |
| `[]` — active,     |                                                                       |
| `[X]` — completed, |                                                                       |
| `[-]` — paused,    |                                                                       |
| `[!]` — canceled   |                                                                       |
| `[priority]`       | Task priority:                                                        |
| `A` — urgent,      |                                                                       |
| `B` — important,   |                                                                       |
| `C` — desirable,   |                                                                       |
| `D` — optional     |                                                                       |
| `task:`            | Description of the task (what needs to be done)                       |
| `start:`           | Start date of execution (format: `YYYYMMDD`)                          |
| `end:`             | Completion date (if the task is finished)                             |
| `due:`             | Deadline for completion                                               |
| `place:`           | Location of execution (e.g., office, home, online)                    |
| `method:`          | Method or tool used (e.g., anki, markdown, quizlet)                   |
| `role:`            | Who performs the task (e.g., `role:other,Ivan`)                       |
| `tags:`            | List of tags (e.g., `tags:work,urgent`) — for filtering and analytics |
| `id:`              | Unique task identifier (e.g., `G001_P02_T05`)                         |


Where:
* `[status]` - indicates the state of the task (e.g., `[]` for active, `[X]` for completed, `[-]` for paused, `[!]` for canceled).
* `[priority]` - optional but recommended attribute, which can be `[A]` (urgent), `[B]` (important), `[C]` (desirable), `[D]` (optional).
* `task:` - keyword indicating that this is a task.
* `Task Name` - a brief description of the action.
* `start:YYYYMMDD` - task start date in `YYYYMMDD` format.
* `due:YYYYMMDD` - task deadline.
* `id:Unique ID` - a unique task identifier that should not be changed after creation. It is recommended to use the `Gxxx_Pxx_Txx` structure.
* `role:role,name` - indicates who is performing the task if it's not you (e.g., `role:other,Marina`).
* `depends:on:<DependencyID>` - indicates a dependency on another task by its ID.
* `method:method` - method or tool for completing the task (e.g., `method:anki`).
* `tags:tag1,tag2` - tags for filtering and sorting (e.g., `tags:focus,urgent`).

## 📌 Rule:

> **If a task depends on another (`depends_on:`), then `depends_on:` must come before `task:`.**
> This emphasizes that the task cannot start until the other one is finished.

**Examples of tasks from the documentation:**

* Completed task with priority: `[X][A] task:eliminate sugar id:G001_P01_T01`.
* Active task with dates and ID: `[] [B] task:write May report start:2025-06-02 due:2025-06-02 id:G002_P01_T01`.
* Task with role and dependency specified: `[][C] task:attach form to report id:G002_P03_T02 depends:on:<G002_P03_T01>`.

This format ensures clarity and machine readability, allowing for easy task tracking and management.
---

### 2. The Main File: `goals_cptd.md`

This file is your control panel. Here, you describe all major goals and break them down into projects and specific tasks.

**Structure:**

- **goals:** — A global objective (e.g., for a quarter or year).
- **project:** — A part of a goal, a major block of work.
- **task:** — A specific action that needs to be performed.

**Example:**


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
[*][A] start:2025-07-14 task:create backup server 192.150.0.120 due:2025-07-16
[*][A] depends_on:G019_P02_T01 start:2025-06-20 task:add new license cryptoprotos method:server due:2025-06-25 id:G019

--------TASK DAILY--------------

[X][A] task:eliminate sugar start:2025-06-01 end:2025-06-01 due:2025-06-01 id:G001_P01_T01
[X][B] task:call new client start:2025-06-01 due:2025-06-01 id:G002_P02_T01
[X][C] task:learn 20 words start:2025-06-01 due:2025-06-01 method:quizlet id:G003_P01_T01
[][B] depends_on:G001_P02_T01 task:write May report start:2025-06-02 due:2025-06-02 id:G002_P01_T01
[][A] task:go to bed before 23:00 start:2025-06-03 due:2025-06-03 id:G001_P02_T01

[][B]task:Buy groceries start:20250612 duration:1h place:store  
[X][C]task:Pick up package from post office start:20250611 end:20250612 duration:30m place:post_office  
[][A]task:Review team reports start:20250612 duration:2h place:office  

[X][B]task:Study modal verbs start:20250608 end:20250612 duration:3d place:home id:G002_P01_T02  
[][C]task:Take Quizlet test start:20250610 duration:20m method:online id:G002_P02_T02  
[][B]task:Write an essay on "Mein Tag" start:20250612 duration:1.5h place:home id:G002_P03_T01  

[][C]task:Make a dentist appointment start:20250612 method:phone  
[X][C]task:Create a project backup start:20250612 end:20250612 duration:15m method:workstation  
[][B]task:Prepare presentation slides start:20250612 duration:2h place:office  
[][B]task:Learn 100 A2-level words start:20250611 duration:3d place:home id:G002_P02_T03  


```

### 4. Archiving: `archive_cptd.md`

When a goal is fully achieved (all its projects and tasks are completed), it is moved from `goals_cptd.md` to `archive_cptd.md`. When archiving, the goal, projects, and tasks are removed from the main `goals_cptd.md` file.

**Archive Example:**



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
