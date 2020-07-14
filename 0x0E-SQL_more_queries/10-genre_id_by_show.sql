-- Find the show and genre
-- Maybe I'm missing a comment
SELECT tv_shows.title, tv_show_genres.genre_id from tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
