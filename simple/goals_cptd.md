### [][A] goals:health id:G001 status:active progress:2/4

    [][A] project:nutrition id:G001_P01 progress:2/2
        [X][A] task:eliminate sugar id:G001_P01_T01
        [X][B] task:drink 2L of water per day id:G001_P01_T02
    [][B] project:sleep id:G001_P02 progress:0/2
        [][C] task:go to bed before 23:00 id:G001_P02_T01
        [][B] task:don't use phone after 22:00 id:G001_P02_T02

### [][B] goals:work id:G002 status:active progress:1/3
    [][A] project:reports id:G002_P01 progress:0/1
        [][] task:write May report id:G002_P01_T01
    [][B] project:clients id:G002_P02 progress:1/1
        [X][B] task:call new client id:G002_P02_T01
    [][A] project:accounting id:G002_P03 progress:0/2
        [][A] task:request tax form id:G002_P03_T01 role:other,Marina
        [][C] task:attach form to report id:G002_P03_T02 depends:on:<G002_P03_T01>
