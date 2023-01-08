CREATE INDEX software_fbt_index ON software(publisher, TRUNC(expire_date, 'YEAR'));
DROP INDEX software_fbt_index;
