SELECT COUNT(*) FROM (
    SELECT r.room_id, COUNT(*) FROM room r
    JOIN building b ON r.building_id = b.building_id
    JOIN computer cp ON r.room_id = cp.room_id
    JOIN cpu_pr c ON cp.computer_id = c.computer_id
    WHERE LOWER(b.country) IN ('costa rica', 'luxembourg', 'rileyshire', 'australia')
    AND c.min_clock_speed > 2.5
    AND c.max_clock_speed > 3.5
    AND r.floor = 3
    GROUP BY r.room_id
);
