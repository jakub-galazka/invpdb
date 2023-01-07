CREATE BITMAP INDEX computer_fbm_index ON computer(UPPER(computer_name), manufacturer);
DROP INDEX computer_fbm_index;
