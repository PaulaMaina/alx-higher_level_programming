-- Lists all shows that have at least one genre linked
SELECT tv_shows.title, tv_genres.genre_id
FROM tv_shows
INNER JOIN tv_genres
ON tv_shows.id=tv_genres.show_id
ORDER BY tv_shows.title, tv_genres.genre_id;
