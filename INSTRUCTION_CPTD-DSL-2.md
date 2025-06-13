
## Guide to Using the CPTD System

CPTD is a text-based system for managing goals, projects, and tasks. It helps you structure your plans, track progress, and maintain daily logs in simple `.md` files.

### 1. File Structure

It is recommended to store all files in a single folder, organized by year.

```
📁 2025/
├── goals_cptd.md         ← general structure: goals, projects, tasks
├── archive_cptd.md       ← archive of all completed goals
├── activ_cptd.md         ← single active task and habit log file
├── dictionary_cpdt.md    ← dictionary of all terms and parameters
├── user_manifest.cptd    ← user profile and settings
```

⚠️ **Daily files like `2025-06-01.cptd.md` are no longer used in CPTD-DSL-2.**  
All active tasks and habits are tracked in `activ_cptd.md`.

---

For a task in the CPTD system, the general format is as follows:

```
[status][priority] depends_on:<TaskID> task:Task Name start:YYYY-MM-DD due:YYYY-MM-DD end:YYYY-MM-DD place:Location method:Tool role:role,name tags:tag1,tag2 id:UniqueID
```

|Element|Meaning|
|---|---|
|`depends_on:`|ID of another task that this task depends on|
|`[status]`|Task status:|
|`[]` — active||
|`[X]` — completed||
|`[-]` — paused||
|`[!]` — canceled||
|`[priority]`|Task priority:|
|`A` — urgent||
|`B` — important||
|`C` — desirable||
|`D` — optional||
|`task:`|Description of the task (what needs to be done)|
|`start:`|Start date of execution (format: `YYYYMMDD`)|
|`end:`|Completion date (if the task is finished)|
|`due:`|Deadline for completion|
|`place:`|Task location (e.g., office, home, online)|
|`method:`|Method or tool used (e.g., anki, markdown, quizlet)|
|`role:`|Who performs the task (e.g., `role:other,Ivan`)|
|`tags:`|List of tags (e.g., `tags:work,urgent`) — for filtering and analytics|
|`id:`|Unique task identifier (e.g., `G001_P02_T05`)|

## 📌 Rule:

> **If a task depends on another (`depends_on:`), then `depends_on:` must come before `task:`.**  
> This emphasizes that the task cannot start until the other one is finished.

### Examples of tasks from the documentation:

- `[X][A] task:eliminate sugar id:G001_P01_T01`
    
- `[][B] task:write May report start:2025-06-02 due:2025-06-02 id:G002_P01_T01`
    
- `[][C] depends_on:G002_P03_T01 task:attach form to report id:G002_P03_T02`
    

This format ensures clarity and machine readability, allowing for easy task tracking and management.

---

### 2. The Main File: `goals_cptd.md`

This file is your control panel. Here, you describe all major goals and break them down into projects and specific tasks.

**Structure:**

- `goals:` — A global objective (e.g., for a quarter or year).
    
- `project:` — A part of a goal, a major block of work.
    
- `task:` — A specific action that needs to be performed.
    

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

---

### 3. Active File: `activ_cptd.md`

All current work is tracked in a single active file `activ_cptd.md`, which replaces daily logs.

**Structure:**

```
----- DAILY -----
[]habit:review code
[]habit:check email

------TASK DAILY------
[][A] task:buy domain name cptdcli.com start:2025-06-13 due:2025-06-19 id:G001_P03_T01

------FUTURE TASK------
[*][A] depends_on:G001_P02_T01 task:create command grep due:2025-06-19 id:G001_P02_T02
```

Tasks remain in this file until marked as completed (`[X]`), after which they are transferred to the archive.

---

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

[X][A] task:write description of the CPTD CLI project start:2025-06-10 end:2025-06-10
[X][B] task:check syntax of all tasks in activ_cptd.md start:2025-06-11 end:2025-06-11
[X][C] task:reply to user email with installation questions start:2025-06-12 end:2025-06-12
[X][A] task:upload CPTD-DSL-2 instruction to the server start:2025-06-13 end:2025-06-13
```

---

### 5. Recommendations for Maintaining Files

- **Structure:** Store all `.cptd.md` files in a separate directory, organized by year or project.
    
- **Identifiers (ID):** Use the `Gxxx_Pxx_Txx` structure. Do not change an ID after its creation.
    
- **Working with Tasks:** Do not delete tasks, even canceled ones—mark them with `[!]`.
    
- **Progress:** Manually update the `progress:x/y` field in `goals_cptd.md` when the status of tasks changes.
    
- **Syntax:** Maintain a consistent order of parameters (`status priority start_date task id deadline...`) for readability.
    
- **Dates:** Always use the `YYYY-MM-DD` format.
    
- **Active file:** Only use `activ_cptd.md` for tracking — daily files are deprecated in CPTD-DSL-2.
    
- **Archiving:** Move `[X]` tasks to `archive_cptd.md` regularly to keep the active file clean.
    

---
