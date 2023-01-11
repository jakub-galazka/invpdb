CREATE TABLE software_ph
(
    software_id   number(7), 
    software_name char(50) NOT NULL, 
    publisher     char(50) NOT NULL, 
    license_key   char(15), 
    expire_date   date, 
    PRIMARY KEY (software_id)
)
    PARTITION BY HASH (publisher)
    PARTITIONS 8;