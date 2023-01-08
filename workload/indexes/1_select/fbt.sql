CREATE INDEX computer_fbt_index ON computer ((hdd_memory - ssd_memory) DESC, hdd_memory, ssd_memory);
DROP INDEX computer_fbt_index;
