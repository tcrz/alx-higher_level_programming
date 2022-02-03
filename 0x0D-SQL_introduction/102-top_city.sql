-- Import in hbtn_0c_0 database this table dump: sql file
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, avg(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city having avg_temp > 73 ORDER BY avg_temp desc;
