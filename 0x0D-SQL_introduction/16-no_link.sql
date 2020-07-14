-- Now we are going to exclude people without names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
