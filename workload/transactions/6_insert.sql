/*
    Assign users to computers with average components:
    ssd_memory, GPU tgp, CPU cores_numerb, RAM stick memory >= AVG
*/
INSERT INTO workplace (computer_id, room_id, account_id)
SELECT cp.computer_id, cp.room_id, a.account_id FROM computer cp
JOIN room r ON cp.room_id = r.room_id
JOIN building b ON r.building_id = b.building_id
JOIN account_building ac ON b.building_id = ac.building_id
JOIN account a ON ac.account_id = a.account_id
JOIN cpu c ON cp.computer_id = c.cpu_id
JOIN gpu g ON cp.computer_id = g.gpu_id
JOIN ram_stick rs ON cp.computer_id = rs.computer_id
WHERE cp.ssd_memory >= (SELECT AVG(ssd_memory) FROM computer)
AND g.tgp >= (SELECT AVG(tgp) FROM gpu)
AND c.cores_number >= (SELECT AVG(cores_number) FROM cpu)
AND rs.memory >= (SELECT AVG(memory) FROM ram_stick);
ROLLBACK;
