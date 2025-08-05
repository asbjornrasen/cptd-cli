
from pathlib import Path
import argparse, yaml, subprocess, sys, shutil, json, os
from cptd_tools.syntax_utils import print_help

SYNTAX = {
    "name": "gitauto",
    "description": "Run git commands defined in a YAML workflow file",
    "usage": "cptd gitauto [options]",
    "arguments": [
        {"name": "--file", "required": False, "help": "YAML workflow file"},
        {"name": "--add-yaml", "required": False, "help": "Copy YAML file to workflow directory"},
        {"name": "--del-yaml", "required": False, "help": "Delete YAML file from workflow directory"},
        {"name": "--set-path", "required": False, "help": "Set custom workflow directory"},
        {"name": "--reset-path", "required": False, "help": "Reset workflow directory to default"},
        {"name": "--list", "required": False, "help": "List available workflow YAMLs"},
        {"name": "--dry-run", "required": False, "help": "Show commands without executing"},
        {"name": "--log", "required": False, "help": "Log output to a file"},
        {"name": "--summary", action": "store_true", "help": "Show summary at the end"},
        {"name": "--edit", "required": False, "help": "Edit a YAML file in default editor"}
    ],
    "examples": [
        "cptd gitauto --file deploy.yaml",
        "cptd gitauto --add-yaml myfile.yaml",
        "cptd gitauto --log out.txt --file deploy.yaml --summary"
    ]
}

def get_config_file():
    return Path(__file__).parent / "workflow_config.json"

def get_workflow_path():
    config = get_config_file()
    if config.exists():
        try:
            data = json.loads(config.read_text(encoding="utf-8"))
            return Path(data.get("workflow_path"))
        except:
            pass
    return Path(__file__).parent / "workflow"

def run(argv):
    if "--help" in argv or "-h" in argv:
        print_help(SYNTAX)
        return

    parser = argparse.ArgumentParser("cptd gitauto", add_help=False)
    parser.add_argument("--file", type=str)
    parser.add_argument("--add-yaml", type=str)
    parser.add_argument("--del-yaml", type=str)
    parser.add_argument("--set-path", type=str)
    parser.add_argument("--reset-path", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log", type=str)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--edit", type=str)

    try:
        args = parser.parse_args(argv)
    except Exception as e:
        print(f"[!] Argument error: {e}")
        print_help(SYNTAX)
        return

    config_file = get_config_file()
    workflow_dir = get_workflow_path()
    workflow_dir.mkdir(parents=True, exist_ok=True)

    if args.set_path:
        config_file.write_text(json.dumps({"workflow_path": args.set_path}, indent=2))
        print(f"[✔] Workflow path set to: {args.set_path}")
        return

    if args.reset_path:
        if config_file.exists():
            config_file.unlink()
            print("[✔] Workflow path reset to default")
        else:
            print("[ℹ] Workflow path was already default")
        return

    if args.add_yaml:
        src = Path(args.add_yaml)
        if not src.exists():
            print(f"[✘] File not found: {src}")
            return
        shutil.copy(src, workflow_dir / src.name)
        print(f"[✔] YAML copied to: {src.name}")
        return

    if args.del_yaml:
        tgt = workflow_dir / args.del_yaml
        if tgt.exists():
            tgt.unlink()
            print(f"[✔] Deleted: {tgt.name}")
        else:
            print(f"[✘] File not found: {tgt}")
        return

    if args.list:
        print(f"📂 Available YAMLs in {workflow_dir}:
")
        for f in workflow_dir.glob("*.yaml"):
            print("  •", f.name)
        return

    if args.edit:
        target = workflow_dir / args.edit
        if not target.exists():
            print(f"[✘] File not found: {target}")
            return
        os.system(f'"{os.environ.get("EDITOR", "nano")}" "{target}"')
        return

    
    if "--example" in argv:
        example_path = workflow_dir / "example.yaml"
        example_content = """name: "Example Git Workflow"
repo: "/path/to/your/repo"
steps:
  - name: "Pull"
    command: "git pull"
    args: ["origin", "main"]
  - name: "Add"
    command: "git add"
    args: ["."]
  - name: "Commit"
    command: "git commit"
    args: ["-m", "Template commit"]
  - name: "Push"
    command: "git push"
    args: ["origin", "main"]
"""
        example_path.write_text(example_content)
        print(f"[✔] Example written to: {example_path}")
        return

    if args.file:
        yaml_path = workflow_dir / args.file
        if not yaml_path.exists():
            print(f"[✘] File not found: {yaml_path}")
            return

        from util.runner import execute_workflow
        execute_workflow(yaml_path, dry_run=args.dry_run, log_path=args.log, summary=args.summary)
        return

    print_help(SYNTAX)
