CREATE BITMAP INDEX computer_hdd_ssd_memory_fbm ON computer ((hdd_memory - ssd_memory) DESC, hdd_memory, ssd_memory);
DROP INDEX computer_hdd_ssd_memory_fbm;
