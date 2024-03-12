-- Lists all records of second_table
-- Results should display both score and the name(in this order)
-- Records should be ordered by score
SELECT score, name
FROM second_table
WHERE score>=10
ORDER BY score DESC, name ASC;
