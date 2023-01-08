DELETE FROM computer
WHERE computer_id IN (
    SELECT cp.computer_id FROM computer cp
    JOIN cpu c ON cp.computer_id = c.computer_id
    JOIN gpu g ON cp.computer_id = g.computer_id
    WHERE UPPER(cp.computer_name) < 'G'
    AND cp.manufacturer LIKE 'ThinkPad%'
    AND c.memory = 1
    AND g.tgp < 50
);
