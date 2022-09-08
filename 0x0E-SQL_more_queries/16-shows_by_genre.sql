-- lists all shows & all genres linked to that show, from db
SELECT tvs.title, tg.name
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tsg
ON tvs.id = tsg.show_id
LEFT JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
ORDER BY tvs.title ASC, tg.name ASC;
