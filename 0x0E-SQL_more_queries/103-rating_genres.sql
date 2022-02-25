-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name, sum(tv_show_ratings.rate) AS rating
FROM tv_genres, tv_show_genres, tv_shows, tv_show_ratings
WHERE tv_genres.id=tv_show_genres.genre_id
AND tv_show_genres.show_id=tv_shows.id AND tv_shows.id=tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
