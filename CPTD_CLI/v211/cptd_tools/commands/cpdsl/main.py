
from cptd_tools.os_guard import ensure_compatible
ensure_compatible(__file__)

from cptd_tools.syntax_utils import print_help
import subprocess
import argparse
import yaml
import os
from pathlib import Path

SYNTAX = {
    "name": "cpdsl",
    "description": "Interprets and runs .dsl scenario files using installed cptd commands.",
    "usage": "cptd cpdsl run <scenario.dsl> [--log file] [--strict] [--wait-all]",
    "arguments": [
        {"name": "run", "required": False, "help": "Run the given DSL file"},
        {"name": "validate", "required": False, "help": "Check if the DSL file is valid"},
        {"name": "--log", "required": False, "help": "Path to write execution log"},
        {"name": "--strict", "required": False, "help": "Stop on first failure"},
        {"name": "--wait-all", "required": False, "help": "Wait for all async tasks to complete"}
    ],
    "examples": [
        "cptd cpdsl run backup.dsl",
        "cptd cpdsl run deploy.dsl --log out.txt --strict"
    ]
}

def run(argv):
    if "--help" in argv or "-h" in argv or not argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser(description=SYNTAX["description"], add_help=False)
    parser.add_argument("action", choices=["run", "validate"])
    parser.add_argument("file", type=Path)
    parser.add_argument("--log", type=str)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--wait-all", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args(argv)

    if not args.file.exists():
        print(f"[!] File not found: {args.file}")
        return

    try:
        with args.file.open("r", encoding="utf-8") as f:
            dsl = yaml.safe_load(f)
    except Exception as e:
        print(f"[!] YAML parse error: {e}")
        return

    if args.action == "validate":
        print("[✔] DSL file is valid.")
        return

    steps = dsl.get("steps", [])
    processes = []
    step_results = {}

    def log(msg):
        print(msg)
        if args.log:
            with open(args.log, "a", encoding="utf-8") as logf:
                logf.write(msg + "\n")

    for i, step in enumerate(steps, 1):
        name = step.get("name", f"Step {i}")
        command = step["command"]
        args_dict = step.get("args", {})
        is_async = step.get("async", False)
        depends_on = step.get("depends_on", [])
        if isinstance(depends_on, str):
            depends_on = [depends_on]

        failed = False
        for dep in depends_on:
            if dep not in step_results:
                log(f"[✖] Step '{name}' depends on unknown step '{dep}'")
                return
            if step_results[dep] != 0:
                log(f"[✖] Step '{name}' skipped due to failed dependency '{dep}'")
                step_results[name] = -1
                failed = True
                break
        if failed:
            continue

        cmd = ["cptd", command]
        for k, v in args_dict.items():
            if isinstance(v, bool):
                if v:
                    cmd.append(k)
            else:
                cmd.extend([k, str(os.environ.get(v) if k.endswith("-env") else v)])

        log(f"[→] {name}: {' '.join(cmd)}")
        if is_async:
            proc = subprocess.Popen(cmd)
            processes.append((name, proc))
            step_results[name] = None
            log(f"[…] Step running asynchronously: {name}")
        else:
            result = subprocess.run(cmd)
            step_results[name] = result.returncode
            if result.returncode != 0:
                log(f"[✖] Step failed: {name}")
                if args.strict:
                    log("[!] Execution stopped due to --strict mode.")
                    return

    if args.wait_all:
        if not processes:
            log("[✔] No async tasks to wait — execution complete.")
        else:
            log("[⏳] Waiting for all async tasks to complete...")
            for name, proc in processes:
                proc.wait()
                code = proc.returncode
                step_results[name] = code
                if code == 0:
                    log(f"[✔] Async step completed: {name}")
                else:
                    log(f"[✖] Async step failed: {name}")
                    if args.strict:
                        log("[!] Execution stopped due to --strict mode.")
                        return
            log("[✔] All async steps completed successfully.")

    if args.summary:
        log("\nSummary:")
        for i, step in enumerate(steps, 1):
            name = step.get("name", f"Step {i}")
            result = step_results.get(name)
            if result == 0:
                log(f"✔ {name:<25} [OK]")
            elif result is None:
                log(f"… {name:<25} [ASYNC]")
            elif result == -1:
                log(f"↷ {name:<25} [SKIPPED]")
            else:
                log(f"✖ {name:<25} [FAILED]")
