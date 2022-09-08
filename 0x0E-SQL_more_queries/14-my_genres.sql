-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name AS name
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg
ON tsg.genre_id = tg.id
JOIN tv_shows AS tvs
ON tsg.show_id = tvs.id
WHERE tvs.title = 'Dexter'
ORDER BY tg.name ASC;
