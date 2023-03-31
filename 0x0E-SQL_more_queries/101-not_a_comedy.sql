-- ists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title, results in ascending order
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
      (SELECT tvs.title
      FROM tv_shows AS tvs
      JOIN tv_show_genres AS tsg
      ON tvs.id = tsg.show_id
      JOIN tv_genres AS tg
      ON tsg.genre_id = tg.id
      WHERE tg.name = 'Comedy')
ORDER BY tv_shows.title ASC;
