-- script that displays the max temperature of each state (ordered by State name)
-- used: temperature table
SELECT state, max(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
