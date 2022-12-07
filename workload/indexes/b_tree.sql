-- For 1_select
CREATE INDEX cpu_cores_number_index ON cpu (cores_number);
CREATE INDEX computer_ssd_memory_index ON computer (ssd_memory);
CREATE INDEX computer_hdd_memory_index ON computer (hdd_memory);

-- For 4_update
CREATE INDEX room_floor_index ON room (floor);
CREATE INDEX software_publisher_index ON software (publisher);

-- For 5_delete
CREATE INDEX building_country_index ON building (LOWER(country));
CREATE INDEX gpu_memory_index ON gpu (memory);
CREATE INDEX gpu_tgp_index ON gpu (tgp);
