-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tvs.title, tsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tsg
ON tvs.id = tsg.show_id
WHERE tsg.genre_id IS NULL
ORDER BY tvs.title, tsg.genre_id ASC;
