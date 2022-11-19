-- Display room_id and room_name of rooms on the first floor of the building with more than 2 computers.
SELECT COUNT(*) FROM (
    SELECT r.room_id, r.room_name FROM room r
    WHERE r.building_id = 100
    AND r.floor = 1
    AND (SELECT COUNT(*) FROM computer WHERE room_id = r.room_id) > 2
);
