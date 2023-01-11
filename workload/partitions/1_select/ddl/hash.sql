CREATE TABLE computer_ph
(
    computer_id   number(7), 
    computer_name char(50) NOT NULL, 
    manufacturer  char(50) NOT NULL, 
    ssd_memory    number(5), 
    hdd_memory    number(5), 
    add_info      char(2000), 
    room_id       number(7) NOT NULL, 
    PRIMARY KEY (computer_id)
)
    PARTITION BY HASH (hdd_memory)
    PARTITIONS 8;
