CREATE BITMAP INDEX software_fbm_index ON software(publisher, TRUNC(expire_date, 'YEAR'));
DROP INDEX software_fbm_index;
