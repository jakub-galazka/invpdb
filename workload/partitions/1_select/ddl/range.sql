CREATE TABLE computer_pr
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
    PARTITION BY RANGE (hdd_memory)
(
    PARTITION p01 VALUES LESS THAN (2001),
    PARTITION p02 VALUES LESS THAN (6001),
    PARTITION p03 VALUES LESS THAN (8001),
    PARTITION p04 VALUES LESS THAN (10001),
    PARTITION p05 VALUES LESS THAN (12001),
    PARTITION p06 VALUES LESS THAN (16001),
    PARTITION p07 VALUES LESS THAN (18001),
    PARTITION p08 VALUES LESS THAN (20001)
);
