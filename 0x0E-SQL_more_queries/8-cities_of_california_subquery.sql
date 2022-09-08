-- lists all the cities of California in db
SELECT id , name 
FROM cities
WHERE state_id IN(
	SELECT id FROM states WHERE name= 'California'
	)
ORDER BY id;

