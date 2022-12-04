/* Assign accounts to the computer (well than average components) and room.
-- Components:
-- SSD MEMORY greater than 2322
-- GPU TPG greater than 85
-- CPU CORES NUMBER greater than 4
RAM STICK MEMORY greater than 21
*/
INSERT INTO workplace (computer_id, room_id, account_id)
SELECT computer.computer_id, computer.room_id, account_id FROM computer
JOIN account ON account.account_id = computer.computer_id
JOIN gpu ON gpu.gpu_id = computer.computer_id
JOIN cpu ON cpu.cpu_id = computer.computer_id
JOIN ram_stick ON ram_stick.ram_stick_id = computer.computer_id
WHERE computer.ssd_memory > (SELECT ROUND(AVG(computer.ssd_memory)) FROM computer)
AND gpu.tgp >= (SELECT ROUND(AVG(gpu.tgp)) FROM gpu)
AND cpu.cores_number >= (SELECT ROUND(AVG(cpu.cores_number)) FROM cpu)
AND ram_stick.memory >= (SELECT ROUND(AVG(ram_stick.memory)) FROM ram_stick);