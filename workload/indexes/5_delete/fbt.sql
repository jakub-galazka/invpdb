CREATE INDEX computer_fbt_index ON computer(UPPER(computer_name), manufacturer);
DROP INDEX computer_fbt_index;
