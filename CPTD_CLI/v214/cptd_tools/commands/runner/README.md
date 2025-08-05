
# cptd gitauto

**cptd gitauto** — это команда для автоматизации работы с Git через YAML-сценарии.

---

## 📦 Установка

```bash
cptd command --add gitauto_final.zip
```

---

## 📄 Пример YAML-файла (`workflow/deploy.yaml`)

```yaml
name: "Deploy Project"
repo: "/path/to/your/repo"
env:
  GIT_AUTHOR_NAME: "Asbjorn"
  GIT_COMMITTER_EMAIL: "asbjorn@cptdcli.com"
steps:
  - name: "Pull latest changes"
    command: "git pull"
    args: ["origin", "main"]

  - name: "Add all files"
    command: "git add"
    args: ["."]

  - name: "Commit"
    command: "git commit"
    args: ["-m", "Automated commit"]

  - name: "Push"
    command: "git push"
    args: ["origin", "main"]
```

---

## 🧩 Поддерживаемые аргументы

| Аргумент         | Назначение                                                |
|------------------|------------------------------------------------------------|
| `--file`         | Запуск указанного YAML-сценария                           |
| `--list`         | Показать доступные YAML-файлы                              |
| `--edit <file>`  | Открыть YAML в системном редакторе                         |
| `--add-yaml`     | Добавить YAML в рабочую директорию                         |
| `--del-yaml`     | Удалить YAML из директории                                 |
| `--set-path`     | Задать пользовательский путь к YAML                        |
| `--reset-path`   | Удалить кастомный путь                                      |
| `--log <path>`   | Сохранять stdout/stderr шагов в лог-файл                   |
| `--dry-run`      | Не выполнять команды, а только показать                    |
| `--summary`      | Показать статус выполнения всех шагов                      |
| `--example`      | Сгенерировать шаблон YAML по умолчанию в `workflow/`       |

---

## 🧪 DSL интеграция

Пример использования с `cpdsl`:

```yaml
name: "Repo Automation"

steps:
  - name: "Run Git Automation"
    command: "gitauto"
    args:
      --file: deploy.yaml
      --summary: true
```
