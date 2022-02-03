-- Import in hbtn_0c_0 database this table dump: sql file
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, avg(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp desc;
