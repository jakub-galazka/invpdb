/*
    Display COMPUTER.COMPUTER_ID, CPU.MANUFACTURER, COMPUTER.ADD_INFO
    for computers in buildings located in Andorra or Kiribati (BUILDING.COUNTRY)
    that have cpu with more than 8 cores (CPU.CORES_NUMBER)
    and COMPUTER.HDD_MEMORY < max COMPUTER.SSD_MEMORY in COMPUTER table
    and COMPUTER.SSD_MEMORY > min COMPUTER.HDD_MEMORY in COMPUTER table
*/
SELECT COUNT(*) FROM (
    SELECT cp.computer_id, c.manufacturer, cp.add_info FROM computer cp
    JOIN room r ON cp.room_id = r.room_id
    JOIN building b ON r.building_id = r.building_id
    JOIN cpu c ON cp.computer_id = c.computer_id
    WHERE (b.country = 'Andorra' OR b.country = 'Kiribati')
    AND c.cores_number > 8
    AND cp.hdd_memory < (SELECT MAX(ssd_memory) FROM computer) 
    AND cp.ssd_memory > (SELECT MIN(hdd_memory) FROM computer) 
);
