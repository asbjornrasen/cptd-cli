## 🔹 List of Basic Commands

The following commands are available in the CPTD CLI:

| Command           | Purpose                                                                 | Avalible |
|--------------     |-------------------------------------------------------------------------|----------|
| `help`            | Show active commands                                                    |  yes     |
| `setpath`         | The path FOLDER PROJECT will be saved in ~/.cptd_config.json            |  yes     |
| `init`            | project initialization, creation of structural files goals_cptd.md,     |  yes      |
|                   | user_manifest.cptd, archive_cptd.md, yyyymmdd_cptd.md                   |          |
| `generate_ignore  | create .cptdignore                                                      |  yes     |
| `parse`           | Parse a CPTD file and display the task structure                        |  yes     |
| `filter`          | Filter tasks by status, type, priority, or date                         |  no      |
| `report`          | Show task statistics (completed, remaining, etc.)                       |  no      |
| `validate`        | Validate the structure of a CPTD file                                   |  no      |
| `carry-over`      | Carry over unfinished tasks to the next day                             |  no      |
| `new-day`         | Create a new daily file with automatic carry-over                       |  no      |
| `archive`         | Archive completed goals and related projects/tasks                      |  no      |
| `idgen`           | Generate a new task ID in the format `id:Gxxx_Pyy_Tzz`                  |  no      |
| `export`          | Convert CPTD data to CSV, HTML, or JSON format                          |  no      |
| `grep`            | Search across CPTD files                                                |  no      |
| `describe`        | Decode task ID, dependencies, roles, and other metadata                 |  no      |

> ⚠️ Note: The CLI is under active development and not yet ready for production use.
