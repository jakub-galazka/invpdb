-- Show room numbers in buildings 1-3, where are located computers, which have software from IBM and CPU memory higher than 8 OR software from Google which is going to expiry after 2024.01.01 
SELECT COUNT(*) FROM (
    SELECT r.room_id, COUNT(*) FROM room r
    JOIN computer cp ON r.room_id = cp.room_id
    JOIN cpu ON cp.computer_id = cpu.computer_id
    JOIN building b ON r.building_id = b.building_id
    JOIN account_building accb ON b.building_id = accb.building_id
    JOIN account ac ON accb.account_id = ac.account_id
    JOIN software_computer sc ON cp.computer_id = sc.computer_id
    JOIN software s ON sc.software_id = s.software_id
    WHERE b.building_id IN (1, 2, 3)
    AND ((s.publisher = 'IBM' AND cpu.memory > 8) OR (s.publisher = 'Google' AND s.expire_date >= TO_DATE('31/12/2023', 'DD/MM/YYYY')))
    GROUP BY r.room_id
);