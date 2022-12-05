/*
    For buildings 1, 2 and 3, count the number of computers in the rooms
    that have CPU memory > 8 
    AND (
        installed software from IBM
        OR
        software from Google whose expire_date >= 31/12/2023
    )
*/
SELECT COUNT(*) FROM (
    SELECT r.room_id, COUNT(*) FROM room r
    JOIN building b ON r.building_id = b.building_id
    JOIN computer cp ON r.room_id = cp.room_id
    JOIN cpu c ON cp.computer_id = c.computer_id
    JOIN software_computer sc ON cp.computer_id = sc.computer_id
    JOIN software s ON sc.software_id = s.software_id
    WHERE b.building_id IN (1, 2, 3)
    AND (
        (
            c.memory > 8
            AND
            s.publisher = 'IBM'
        )
        OR
        (
            s.publisher = 'Google'
            AND
            s.expire_date >= TO_DATE('31/12/2023', 'DD/MM/YYYY')
        )
    )
    GROUP BY r.room_id
);
