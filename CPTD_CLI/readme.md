⚠️ The CLI is still under active development.  
This is a **work in progress** and not intended for production use yet.  
Features may change or break without notice.


For Windows
Install (CPTD_CLI\windows\): 
pip install .

Uninstall:
pip uninstall -y cptd


------------------

🛠️ Developers are welcome to propose new commands for inclusion in the CPTD DSL CLI.  
If you have an idea that fits the philosophy of the tool, feel free to open an issue or submit a pull request.

Best regards, CryptoProtos team.

## 🛠️ How to Propose a New Command for CPTD DSL CLI

To have your command included in the **official CPTD DSL CLI release**, please follow these steps:

---

### ✅ Contribution Guide

1. **Fork** the repository:  
   [CPTD-DSL on GitHub](https://github.com/asbjornrasen/cptd-dsl)

2. **Create a new branch** named after your command, for example:  
   `feature/mycommand`

3. **Add your command file** to the following directory:  
   `CPTD_CLI/cptd_tools/commands/`

4. Make sure your command:
   - follows the style of the project,
   - provides a help option (`--help`),
   - does not break the existing CLI structure.

5. **Open a Pull Request** with a brief description of your command and its purpose.

6. After review and approval, your command will be included in the **official release**.

---

💡 *Tip: Follow the philosophy of the tool — clarity, modularity, and practical utility for daily task management.*

Need help with a command template or code review? Feel free to ask.
