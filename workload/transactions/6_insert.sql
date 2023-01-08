INSERT INTO workplace (computer_id, room_id, account_id)
SELECT cp.computer_id, cp.room_id, a.account_id FROM computer cp
JOIN room r ON cp.room_id = r.room_id
JOIN building b ON r.building_id = b.building_id
JOIN account_building ac ON b.building_id = ac.building_id
JOIN account a ON ac.account_id = a.account_id
JOIN cpu c ON cp.computer_id = c.cpu_id
JOIN ram_stick rs ON cp.computer_id = rs.computer_id
WHERE rs.ram_stick_id < 1000
AND rs.memory < 4 
OR (cp.hdd_memory < 3000 AND c.memory < 2);
