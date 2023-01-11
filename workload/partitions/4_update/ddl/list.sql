CREATE TABLE software_pl
(
    software_id   number(7), 
    software_name char(50) NOT NULL, 
    publisher     char(50) NOT NULL, 
    license_key   char(15), 
    expire_date   date, 
    PRIMARY KEY (software_id)
)
    PARTITION BY LIST (publisher) (
        PARTITION Microsoft VALUES ('Microsoft'),
        PARTITION Mozilla VALUES ('Mozilla'),
        PARTITION Yahoo VALUES ('Yahoo'),
        PARTITION Adobe VALUES ('Adobe'),
        PARTITION Kakao VALUES ('Kakao'),
        PARTITION Foxit VALUES ('Foxit'),
        PARTITION PandoraTV VALUES ('PandoraTV'),
        PARTITION Google VALUES ('Google'),
        PARTITION IMB VALUES ('IBM'),
        PARTITION JetBrains VALUES ('JetBrains')
);
