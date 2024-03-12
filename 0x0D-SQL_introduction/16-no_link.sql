-- Lists all records of second_table
-- Rows should include the name
-- Results should be display the score followed by the name
-- Records should be listed descending score
SELECT score, name
FROM second_table
WHERE CHAR_LENGTH(name) > 0
ORDER BY score DESC;
