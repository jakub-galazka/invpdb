SELECT COUNT(*) FROM (
    SELECT cp.room_id FROM computer cp
    JOIN software_computer sc ON cp.computer_id = sc.computer_id
    JOIN software s ON sc.software_id = s.software_id
    WHERE s.publisher = 'Google'
    AND TRUNC(s.expire_date, 'YEAR') > TO_DATE('2023', 'YYYY')
    AND cp.ssd_memory > cp.hdd_memory
);
