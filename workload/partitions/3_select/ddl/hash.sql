CREATE TABLE cpu_ph
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
    PARTITION BY HASH (min_clock_speed, max_clock_speed)
    PARTITIONS 8;
