PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> ls


    Каталог: E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows


----                 -------------         ------ ----
d-----        11.06.2025      0:33                build
d-----        11.06.2025      1:27                cptd.egg-info
d-----        11.06.2025      1:01                cptd_tools
-a----        11.06.2025      1:23           2950 listing_terminal.md
-a----        11.06.2025      0:29           1175 setup.py


PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> pip install .
Processing e:\cryptoprotos\cptd-dsl\cptd_cli\windows
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: argcomplete>=1.12.0 in c:\users\user44\appdata\local\programs\python\python313\lib\site-packages (from cptd==1.0.0) (3.6.2)
Building wheels for collected packages: cptd
  Building wheel for cptd (pyproject.toml) ... done
  Created wheel for cptd: filename=cptd-1.0.0-py3-none-any.whl size=4416 sha256=6c59893d934bdb5de86f3b1989162712db471d5a9e589fe8253e8afe8bafc92a
  Stored in directory: C:\Users\user44\AppData\Local\Temp\pip-ephem-wheel-cache-fzu2zc_3\wheels\40\de\64\531067bddf658100f29e4d60d68372852f34e12690fea5389a        
Installing collected packages: cptd
Successfully installed cptd-1.0.0
Name: cptd
Version: 1.0.0
Summary: CPTD CLI — инструмент для работы с DSL-планировщиком
Home-page:
Author: Asbjorn Rasen
Author-email: author@example.com
License:
Location: C:\Users\user44\AppData\Local\Programs\Python\Python313\Lib\site-packages
Requires: argcomplete
Required-by:
PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> cptd help

 Доступные команды:
  - parse
  - report
  - template

Пример: cptd report goals_cptd.md
PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> cptd parse "Y:\003_ToDo\2025\20250601_cptd.md"
TASK | X : A | сьездить на склад и отзвониться оттуда Иличу  start:2025-05-31 due:2025-05-31
TASK | * : A | выучить 10 слов английского start:2025-05-31 method:anki
PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> pip uninstall -y cptd
Found existing installation: cptd 1.0.0
Uninstalling cptd-1.0.0:
  Successfully uninstalled cptd-1.0.0
PS E:\cryptoprotos\cptd-dsl\CPTD_CLI\windows> good job :)