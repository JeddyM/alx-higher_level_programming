--  lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tvs.title
FROM tv_shows AS tvs
JOIN tv_show_genres AS tsg
ON tvs.id = tsg.show_id
JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY tvs.title ASC;
