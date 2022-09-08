-- Lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT tvs.title, SUM(tsr.rate) AS rating
FROM tv_shows AS tvs
JOIN tv_show_ratings AS tsr
ON tvs.id = tsr.show_id
GROUP BY tvs.title
ORDER BY rating DESC;
