-- Finding duplicates
SELECT score, COUNT(score) number FROM second_table GROUP BY score HAVING COUNT(score) > 1; 
