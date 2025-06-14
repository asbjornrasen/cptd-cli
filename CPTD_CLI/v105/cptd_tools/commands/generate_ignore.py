from importlib.resources import files
import cptd_tools

def parse_structure_profiles(text):
    profiles = {}
    current_profile = None

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith("@"):
            current_profile = line[1:]
            profiles[current_profile] = []
        elif line.startswith("-") and current_profile:
            profiles[current_profile].append(line[1:].strip())

    return profiles

def run(argv):
    try:
        manifest_path = files(cptd_tools) / 'cptd_manifest.cptd'
        text = manifest_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("[!] Couldn't find cptd_manifest.cptd inside the package.")
        return

    profiles = parse_structure_profiles(text)
    if not profiles:
        print("[!] Field structure_profiles: not found or empty.")
        return

    structure = [f"{profile}/" for profile in profiles]

    ignore_lines = [
        "# Auto-generated .cptdignore based on structure_profiles",
        "*",
        ""
    ] + [f"!{folder}" for folder in structure] + [
        "",
        "# System files",
        ".DS_Store",
        "*.log",
        "*.tmp",
        "*.bak",
        "__pycache__/",
    ]

    with open(".cptdignore", "w", encoding="utf-8") as f:
        f.write("\n".join(ignore_lines))

    print(f"✅ Generated .cptdignore with {len(structure)} included profiles.")
