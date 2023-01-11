CREATE TABLE cpu_pr
(
    cpu_id          number(7), 
    cpu_name        char(50) NOT NULL, 
    manufacturer    char(50) NOT NULL, 
    cores_number    number(2) NOT NULL, 
    threads_number  number(2) NOT NULL, 
    min_clock_speed number(3, 2) NOT NULL, 
    max_clock_speed number(3, 2) NOT NULL, 
    memory          number(2) NOT NULL, 
    computer_id     number(7) NOT NULL, 
    PRIMARY KEY (cpu_id)
)
    PARTITION BY RANGE (min_clock_speed, max_clock_speed)
(
    PARTITION p01 VALUES LESS THAN (2.6, 3.1),
    PARTITION p02 VALUES LESS THAN (2.6, 4.1),
    PARTITION p03 VALUES LESS THAN (2.6, 5.1),
    PARTITION p04 VALUES LESS THAN (3.1, 3.1),
    PARTITION p05 VALUES LESS THAN (3.1, 4.1),
    PARTITION p06 VALUES LESS THAN (3.1, 5.1),
    PARTITION p07 VALUES LESS THAN (3.6, 3.1),
    PARTITION p08 VALUES LESS THAN (3.6, 4.1),
    PARTITION p09 VALUES LESS THAN (3.6, 5.1),
    PARTITION p10 VALUES LESS THAN (4.1, 3.1),
    PARTITION p11 VALUES LESS THAN (4.1, 4.1),
    PARTITION p12 VALUES LESS THAN (4.1, 5.1),
    PARTITION p13 VALUES LESS THAN (4.5, 3.1),
    PARTITION p14 VALUES LESS THAN (4.5, 4.1),
    PARTITION p15 VALUES LESS THAN (4.5, 5.1)
);
