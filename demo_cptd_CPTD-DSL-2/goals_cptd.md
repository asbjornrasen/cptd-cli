### [][A] goals:CPTD DSL / CLI  id:G001

    [][A] project:core id:G001_P01 
        [X][A] task:make install for linux start:2025-06-11 due:2025-06-13 id:G001_P01_T01
        [][A] task:make setpath support in all commands start:2025-06-11 due:2025-06-13 id:G001_P01_T02
    [][B] project:core commands id:G001_P02 
        [X][B] task:create command dashboard start:2025-06-11 due:2025-06-15 id:G001_P02_T01
        [][A] depends_on:G001_P02_T01 task:create command grep due:2025-06-19  id:G001_P02_T02
        [X][A] task:develop a template for creating additional CLI commands due:2025-06-14  id:G001_P02_T03
    [][B] project:websuit id:G001_P03
        [][A] task:buy domain name cptdcli.com start:2025-06-13 due:2025-06-13  id:G001_P03_T01
        [][A] depends_on:G001_P03_T01 task:install wordpress  due:2025-06-16  id:G001_P03_T02
   
       


