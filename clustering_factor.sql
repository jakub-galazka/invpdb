SELECT ui.index_name, ui.clustering_factor, ut.num_rows, ut.blocks
FROM user_indexes ui
JOIN user_tables ut
ON ui.table_name = ut.table_name
WHERE ui.table_name = 'TABLE_NAME'; 
