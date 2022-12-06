/*
    Display the computer_id and the number of its relationships with buildings located in Kiribati or Andorra.
    The computer must meet the following requirements:
    * CPU min_clock_speed > 3.0
    AND (
        * CPU memory > 2
        OR
        * RAM clock_speed in {1000, 1333, 1600, 2400}
    ) 
    OR
    * CPU manufacturer = Intel
*/
SELECT COUNT(*) FROM (
    SELECT cp.computer_id, COUNT(*) FROM computer cp
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    JOIN cpu c ON cp.computer_id = c.computer_id
    JOIN ram_stick rs ON cp.computer_id = rs.computer_id
    WHERE b.country IN ('Kiribati', 'Andorra')
    AND c.min_clock_speed > 3.0
    AND (
        c.memory > 2
        OR
        rs.clock_speed IN (1000, 1333, 1600, 2400)
    )
    OR c.manufacturer = 'Intel'
    GROUP BY cp.computer_id
);
