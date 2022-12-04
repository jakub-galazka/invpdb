/*
    Update expire_date of the user softwares from the list of publishers:
    ['Microsoft', 'Mozilla', 'Yahoo', 'Adobe', 'IBM', 'Google', 'JetBrains']
    if it is earlier than 31/12/2022.
*/
UPDATE software SET expire_date = TO_DATE('01/01/2025', 'DD/MM/YYYY')
WHERE software_id IN (
    SELECT s.software_id FROM software s
    JOIN software_computer sc ON s.software_id = sc.software_id
    JOIN computer cp ON sc.computer_id = cp.computer_id
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = b.building_id
    JOIN account_building ab ON b.building_id = ab.building_id
    JOIN account a ON ab.account_id = a.account_id
    WHERE a.account_id = 4
    AND s.expire_date <= TO_DATE('31/12/2022', 'DD/MM/YYYY')
    AND s.publisher IN ('Microsoft', 'Mozilla', 'Yahoo', 'Adobe', 'IBM', 'Google', 'JetBrains')
);
ROLLBACK;