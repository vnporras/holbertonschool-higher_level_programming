-- 8. Cities of California
USE hbtn_0d_usa;

SELECT cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
