-- Import in hbtn_0c_0 database this table dump: sql file
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, avg(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp desc LIMIT 3;
