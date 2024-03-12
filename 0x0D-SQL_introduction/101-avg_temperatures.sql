-- Displays the average temperatures by city
-- The list is ordered by temperature in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
