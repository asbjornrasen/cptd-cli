Here is the English translation of your official guide for YAML scenarios in `cpdsl`:

---

# 📘 YAML Scenario Guide for `cpdsl`

`cpdsl` is a YAML-based scenario interpreter for sequential and parallel command execution within the **CPTD CLI** system.
Scenarios let you combine complex processes (archiving, encryption, uploading, testing, etc.) into a single descriptive file.

---

## 🧱 Basic File Structure

```yaml
name: "Scenario Name"
description: "Short description of purpose"

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

## 🧩 Field Descriptions

### 🔹 Top-Level Fields:

| Field         | Type   | Purpose                               |
| ------------- | ------ | ------------------------------------- |
| `name`        | string | Human-readable scenario name          |
| `description` | string | Short summary                         |
| `steps`       | list   | Array of step definitions (see below) |

---

### 🔹 Inside `steps[]`:

| Field        | Type               | Required | Purpose                                                          |
| ------------ | ------------------ | -------- | ---------------------------------------------------------------- |
| `name`       | string             | No       | Step name (for display and `depends_on`)                         |
| `command`    | string             | ✅ Yes    | Name of the registered CPTD command                              |
| `args`       | dict `--flag: val` | No       | Arguments for the command. `true` → flag only; `false` → ignored |
| `async`      | bool               | No       | If `true`, runs the step in the background                       |
| `depends_on` | string / list      | No       | Dependencies. Runs only after specified step(s) complete         |

---

### 🔹 Special Feature: Environment Variables

Instead of a fixed value, you can reference an environment variable:

```yaml
args:
  --password-env: SFTP_PASS
```

Inside `cpdsl`, this becomes:

```bash
--password-env <value of SFTP_PASS>
```

---

## ✅ Example of a Simple Scenario

```yaml
name: "Backup"
description: "Mount, archive, and upload archive"

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

## 🧪 Running a Scenario

```bash
cptd cpdsl run backup.dsl --log log.txt --strict --wait-all --summary
```

### 🎛 Run Arguments:

| Argument       | Purpose                                           |
| -------------- | ------------------------------------------------- |
| `--log <file>` | Save execution log                                |
| `--strict`     | Stop on first error                               |
| `--wait-all`   | Wait for all `async: true` steps to finish        |
| `--summary`    | Print a summary table of step statuses at the end |

---

## 📋 Example of Summary Output (`--summary`)

```
Summary:
✔ Step 1 - Mount                [OK]
✔ Step 2 - Archive              [OK]
✔ Step 3 - Upload               [ASYNC]
```

---

## ⚠️ Error Handling

| Scenario                             | Default Behavior | With `--strict` |
| ------------------------------------ | ---------------- | --------------- |
| `depends_on` references unknown step | Error            | Error           |
| Step exits with non-zero code        | Continues        | Stops           |
| Async step fails                     | Logs the error   | Stops           |

---

## 🚀 Writing Tips

* Always assign a unique `name:` to each step
* Use `depends_on` to define logical order
* Use `async: true` for background tasks
* Store your `.dsl` files in `scripts/` or `scenarios/` for project structure

---

Let me know if you'd like this formatted into a `README.md` layout or converted into HTML documentation.
