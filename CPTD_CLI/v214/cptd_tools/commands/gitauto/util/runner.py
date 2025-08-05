
import subprocess, yaml
from pathlib import Path
import os

def execute_workflow(yaml_path: Path, dry_run=False, log_path=None, summary=False):
    try:
        content = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[!] YAML error: {e}")
        return

    repo = content.get("repo")
    steps = content.get("steps", [])
    env_vars = content.get("env", {})

    if not repo or not (Path(repo) / ".git").exists():
        print(f"[✘] Invalid or missing Git repo: {repo}")
        return

    print(f"[✔] Repository: {repo}\n")
    results = []

    for i, step in enumerate(steps, 1):
        name = step.get("name", f"Step {i}")
        cmd = step.get("command")
        args = step.get("args", [])

        if isinstance(args, list):
            full_cmd = f"{cmd} {' '.join(args)}"
        else:
            full_cmd = cmd

        print(f"➡️  {name}")
        if dry_run:
            print(f"   [DRY RUN] {full_cmd}")
            results.append((name, "SKIPPED"))
            continue

        try:
            result = subprocess.run(
                full_cmd,
                shell=True,
                cwd=repo,
                capture_output=True,
                text=True,
                env={**os.environ, **env_vars}
            )
            if log_path:
                with open(log_path, "a", encoding="utf-8") as log:
                    log.write(f"## {name}\n{result.stdout}\n{result.stderr}\n")

            if result.returncode == 0:
                print(result.stdout.strip())
                print("   [✔] Success\n")
                results.append((name, "OK"))
            else:
                print(result.stderr.strip())
                print(f"   [✘] Failed ({result.returncode})\n")
                results.append((name, "FAILED"))
                break
        except Exception as e:
            print(f"   [✘] Exception: {e}")
            results.append((name, "ERROR"))
            break

    if summary:
        print("\nSummary:")
        for i, (name, status) in enumerate(results, 1):
            mark = "✔" if status == "OK" else "✘" if status == "FAILED" else "…"
            print(f" {mark} Step {i}: {name:<20} [{status}]")
