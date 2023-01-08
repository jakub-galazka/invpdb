CREATE BITMAP INDEX computer_fbm_index ON computer ((hdd_memory - ssd_memory) DESC, hdd_memory, ssd_memory);
DROP INDEX computer_fbm_index;
