-- For 1_select
CREATE BITMAP INDEX cpu_cores_number_index ON cpu (cores_number);
CREATE BITMAP INDEX computer_ssd_memory_index ON computer (ssd_memory);
CREATE BITMAP INDEX computer_hdd_memory_index ON computer (hdd_memory);

-- For 4_update
CREATE BITMAP INDEX room_floor_index ON room (floor);
CREATE BITMAP INDEX software_publisher_index ON software (publisher);

-- For 5_delete
CREATE BITMAP INDEX building_country_index ON building (LOWER(country));
CREATE BITMAP INDEX gpu_memory_index ON gpu (memory);
CREATE BITMAP INDEX gpu_tgp_index ON gpu (tgp);
