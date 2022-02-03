-- Import in hbtn_0c_0 database this table dump: sql file
-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
select city, avg(value) as avg_temp from temperatures group by city order by avg_temp desc
