CREATE BITMAP INDEX software_bm_index ON software(publisher, expire_date);
DROP INDEX software_bm_index;
