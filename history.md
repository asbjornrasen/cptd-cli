08/03/2025

Edit readme.md

add new Example code of command 
edit newcommand.py

08/01/2025

Added new information to the readme.md for PIP

Edited repository into command `cptd install` 

REPOS = {
    "windows": "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/windows",
    "linux":   "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/linux",
    "darwin":  "https://raw.githubusercontent.com/asbjornrasen/cptdcli-plugin/main/community_plugin/macos"
}

07/30/2025

# ADD new command  `cptd install`:

---
Sure! Here's the English version of the announcement post for the `cptd install` command:

---

🔧 **New Command: `cptd install`** — *Install and manage CPTD CLI plugins with ease*

🔥 CPTD CLI just got modular!

You can now extend your CLI with official plugin packages using:

```
cptd install --i <command_name>
```

📦 **What `cptd install` can do:**

* 🔍 List all available plugins for your OS:

  ```
  cptd install --list
  ```

* ✅ Install a command:

  ```
  cptd install --i portscanner
  ```

* 🧪 Install with dependencies (if declared in manifest):

  ```
  cptd install --i portscanner --with-deps
  ```

* ⚠ Allow insecure code (e.g., `pip install` inside plugin):

  ```
  cptd install --i portscanner --allow-insecure
  ```

* ❌ Uninstall a command:

  ```
  cptd install --u portscanner
  ```

🧠 Smart logic:

* Automatically detects your OS (`Windows`, `Linux`, `macOS`) and selects the right repository:

  * `https://www.cptdcli.com/repo01`
  * `https://www.cptdcli.com/repo02`
  * `https://www.cptdcli.com/repo03`

* Each plugin is listed in `plugins.json` with `name`, `version`, and `description`.

---

💡 CPTD CLI is now fully extensible. Install only what you need — instantly.

🔗 Try it now:

```bash
cptd install --list
```


