"""
os_guard.py — проверка совместимости команды CPTD CLI с Текущей ОС.

Использование в плагине:
    from cptd_tools.os_guard import ensure_compatible
    ensure_compatible(__file__)
"""
from pathlib import Path
import json, yaml, platform, shutil, sys

# ──────────────────────────────────────────────────────────────
def _normalize(os_name: str) -> str:
    """Приводит системные названия к  linux / windows / macos / all."""
    name = os_name.lower()
    if name.startswith(("win",)):
        return "windows"
    if name.startswith(("darwin", "mac")):
        return "macos"
    if name.startswith(("linux",)):
        return "linux"
    return name                     # для экзотических систем

def _load_manifest(cmd_dir: Path):
    """Читаем manifest.(json|yaml) и возвращаем словарь."""
    for fname in ("manifest.json", "manifest.yaml", "manifest.yml"):
        f = cmd_dir / fname
        if f.exists():
            if f.suffix == ".json":
                return json.loads(f.read_text(encoding="utf-8"))
            else:
                return yaml.safe_load(f.read_text(encoding="utf-8"))
    raise FileNotFoundError("Manifest not found in command folder")

def _self_remove(cmd_dir: Path):
    """Удаляет весь каталог команды — и сам файл, и манифесты."""
    try:
        shutil.rmtree(cmd_dir)
        print(f"[os_guard] Incompatible OS → command removed: {cmd_dir}")
    except Exception as exc:
        print(f"[os_guard] Unable to delete '{cmd_dir}': {exc}")

# ──────────────────────────────────────────────────────────────
def ensure_compatible(entry_file: str) -> None:
    """
    Проверяет, совпадает ли текущая ОС с полем `target` в манифесте.
    При несовпадении удаляет команду и завершает работу `sys.exit(1)`.
    Должна вызываться первой строкой в каждом плагине.
    """
    cmd_dir = Path(entry_file).resolve().parent
    manifest = _load_manifest(cmd_dir)
    wanted   = _normalize(manifest.get("target", "all"))
    current  = _normalize(platform.system())

    if wanted not in ("all", current):
        print(f"[os_guard] '{manifest['name']}' supports {wanted.upper()} — "
              f"current OS is {current.upper()}.")
        _self_remove(cmd_dir)
        sys.exit(1)

def is_compatible(manifest: dict) -> bool:
    """True, если manifest['target'] совпадает с текущей ОС."""
    wanted  = _normalize(manifest.get("target", "all"))
    current = _normalize(platform.system())
    return wanted in ("all", current)
