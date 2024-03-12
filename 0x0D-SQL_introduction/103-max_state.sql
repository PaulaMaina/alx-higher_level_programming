-- Displays the max temperature of each state
-- The list is ordered by state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
