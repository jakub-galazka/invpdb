DELETE FROM computer
WHERE computer_id IN (
    SELECT cp.computer_id FROM computer cp
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    JOIN gpu g ON cp.computer_id = g.computer_id
    WHERE LOWER(b.country) = 'costa rica'
    AND g.memory > (SELECT MAX(tgp) / 4 FROM gpu)
);
