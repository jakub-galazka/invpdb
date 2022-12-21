SELECT COUNT(*) FROM (
    SELECT cp.room_id, cp.computer_id, cp.computer_name, cp.ssd_memory, cp.hdd_memory, cp.add_info FROM computer cp
    WHERE cp.room_id = 2211
    AND (
        (SELECT COUNT(*) FROM cpu WHERE computer_id = cp.computer_id) > 1
        OR
        (SELECT COUNT(*) FROM gpu WHERE computer_id = cp.computer_id) > 1
        OR
        (SELECT COUNT(*) FROM ram_stick WHERE computer_id = cp.computer_id) > 2
    )
);
