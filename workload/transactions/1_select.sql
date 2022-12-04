-- Show each computer which has CPU.min_clock_speed greather than 3.0 and simultenously CPU.memory greather than 2 or RAM.clock_speed equal to 1000, 1333, 1600, 2400, OR CPU.manufacturer is Intel and bulding where computer is located is in Kiribati or Andorra 
SELECT COUNT(*) FROM (
    SELECT cp.computer_id, COUNT(*) FROM computer cp
    JOIN cpu ON cp.computer_id = cpu.computer_id
    JOIN ram_stick ram ON cp.computer_id = ram.computer_id
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    JOIN account_building accb ON b.building_id = accb.building_id
    JOIN account ac ON accb.account_id = ac.account_id
    WHERE cpu.min_clock_speed > 3.0
    AND (cpu.memory > 2 OR ram.clock_speed IN (1000, 1333, 1600, 2400))
    OR (cpu.manufacturer = 'Intel' AND b.country IN ('Kiribati', 'Andorra'))
    GROUP BY cp.computer_id
);
