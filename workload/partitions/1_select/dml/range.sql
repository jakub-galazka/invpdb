SELECT COUNT(*) FROM (
    SELECT cp.computer_id, cp.add_info FROM computer_pr cp
    JOIN software_computer sc ON cp.computer_id = sc.computer_id
    JOIN software s ON sc.software_id = s.software_id
    WHERE s.expire_date < TO_DATE('31/12/2020', 'DD/MM/YYYY')
    AND (cp.hdd_memory - cp.ssd_memory) < 15000 AND cp.hdd_memory > 10000 AND cp.ssd_memory > 1000
);
