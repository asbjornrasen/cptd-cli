

# 📦 Команда `command` — управление CLI-командами в CPTD DSL

Команда `cptd command` позволяет **добавлять** и **удалять** пользовательские команды в систему CPTD DSL, напрямую взаимодействуя с установленной директорией `cptd_tools/commands`.

---

## 🔹 Синтаксис

```bash
cptd command --add <путь_к_файлу.py>
cptd command --del <имя_файла.py>
````

---

## 📥 Добавление команды

Добавляет указанный `.py`-файл в директорию команд CLI (`site-packages/cptd_tools/commands/`). После этого команда становится доступной в CLI:

### ✅ Пример

```bash
cptd command --add hello.py
cptd hello --name Асбйорн
```

### ⚠️ Требования:

- Имя файла определяет имя команды (`hello.py` → `cptd hello`)
    
- В файле должна быть функция:
    

```python
def run(argv):
    ...
```

- Рекомендуется наличие структуры `SYNTAX = {...}` для отображения справки (`--help`)
    

---

## 🗑 Удаление команды

Удаляет команду (файл `.py`) из установленной директории.

### ✅ Пример

```bash
cptd command --del hello.py
```

> Нельзя удалить встроенную команду `command.py`.

---

## 📂 Где хранятся команды?

Система автоматически определяет установленную директорию с помощью:

```bash
python -c "import cptd_tools.commands as c; print(c.__file__)"
```

Все команды копируются и удаляются именно оттуда.

---

## 🧪 Пример команды `hello.py`

```python
# hello.py

SYNTAX = {
    "name": "hello",
    "description": "Say hello to the user",
    "usage": "cptd hello [--name <имя>]",
    "arguments": [
        {"name": "--name", "required": False, "help": "Кому сказать привет"}
    ],
    "examples": [
        "cptd hello",
        "cptd hello --name Асбйорн"
    ]
}

def run(argv):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="World")
    args = parser.parse_args(argv)
    print(f"Привет, {args.name}!")
```

---

## 👨‍💻 Для разработчиков CPTD-плагинов

1. Создайте файл с функцией `run(argv)` и переменной `SYNTAX`.
    
2. Добавьте его:
    
    ```bash
    cptd command --add mycommand.py
    ```
    
3. Проверьте: `cptd mycommand`
    
4. При желании попасть в основной релиз отправьте Pull Request.
    

---

## 🧠 Полезные советы

- Используйте `python -m py_compile <файл.py>` перед добавлением.
- Это проверит синтаксис! - ВАЖНО!
    
- Избегайте имён `del.py`, `class.py`, `import.py` — это ключевые слова.
- Старайтесь согласовывать имена с основным официальным списком команд CLI.
    
- Вы можете создавать автогенераторы и пакеты команд.
    

---

© CryptoProtos CPTD DSL — 2025
