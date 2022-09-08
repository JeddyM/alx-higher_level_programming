-- ists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title, results in ascending order
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
      (SELECT tg.name AS name
      FROM tv_genres AS tg
      JOIN tv_show_genres AS tsg
      ON tsg.genre_id = tg.id
      JOIN tv_shows AS tvs
      ON tsg.show_id = tvs.id
      WHERE tvs.title = 'Dexter')
ORDER BY tv_genres.name ASC;
