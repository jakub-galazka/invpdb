UPDATE software SET expire_date = TO_DATE('01/01/2025', 'DD/MM/YYYY')
WHERE software_id IN (
    SELECT s.software_id FROM software_pl s
    JOIN software_computer sc ON s.software_id = sc.software_id
    JOIN computer cp ON sc.computer_id = cp.computer_id
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    WHERE r.floor < (SELECT AVG(floors_number) / 2 FROM building)
    AND (s.publisher = 'Microsoft' OR s.publisher = 'Adobe' OR s.publisher = 'IBM')
);
