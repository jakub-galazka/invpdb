-- For 1_select
CREATE BITMAP INDEX cpu_cores_number_index ON cpu (cores_number);
CREATE BITMAP INDEX computer_ssd_memory_index ON computer (ssd_memory);
CREATE BITMAP INDEX computer_hdd_memory_index ON computer (hdd_memory);
