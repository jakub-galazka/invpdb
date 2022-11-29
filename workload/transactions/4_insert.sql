-- Duplicate software from Microsoft, Adobe and IBM.
INSERT INTO software (software_id, software_name, publisher, license_key, expire_date)
SELECT software_id + (SELECT COUNT(*) FROM software), software_name, publisher, license_key, expire_date FROM software
WHERE publisher IN ('Microsoft', 'Adobe', 'IBM');
ROLLBACK;
