/* 
    Remove computers from the second-to-last floor of the building
    that have a processor with less than 3 cores
    and whose min_clock_speed is lower than the average of all computers in that building.
*/
DELETE FROM computer
WHERE computer_id IN (
    SELECT cp.computer_id FROM computer cp
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    JOIN cpu c ON cp.computer_id = c.computer_id
    JOIN gpu g ON cp.computer_id = g.computer_id
    WHERE b.building_id = 1
    AND r.floor = (b.floors_number - 1)
    AND c.cores_number <= 2
    AND c.min_clock_speed < (
        SELECT AVG(ic.min_clock_speed) FROM cpu ic
        JOIN computer icp ON ic.computer_id = icp.computer_id
        JOIN room ir ON ir.room_id = icp.room_id
        WHERE ir.building_id = 1
    )
);
ROLLBACK;
