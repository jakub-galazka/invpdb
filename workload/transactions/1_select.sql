-- View the number of RTX or GTX or R Series GPUs in each room of the building.
SELECT COUNT(*) FROM (
    SELECT r.room_id, COUNT(*) FROM room r
    JOIN computer cp ON r.room_id = cp.room_id
    JOIN gpu g ON cp.computer_id = g.computer_id
    WHERE r.building_id = 250
    AND g.gpu_name LIKE '%RTX%' OR g.gpu_name LIKE '%GTX%' OR g.gpu_name LIKE '%R%'
    GROUP BY r.room_id
);
