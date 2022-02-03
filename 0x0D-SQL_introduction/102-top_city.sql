-- Import in hbtn_0c_0 database this table dump: sql file
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, avg(value) as avg_temp from temperatures WHERE month > 6 AND  month < 9 GROUP BY city HAVING avg_temp > 73 ORDER BY avg_temp DESC;
