-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title FROM tv_shows
WHERE title NOT IN (
	SELECT tv_shows.title from tv_shows, tv_show_genres, tv_genres
	WHERE tv_shows.id=tv_show_genres.show_id AND tv_show_genres.genre_id=tv_genres.id AND tv_genres.name="Comedy"
	)
ORDER BY tv_shows.title ASC;
