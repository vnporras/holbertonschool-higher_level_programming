-- Genre ID by show
SELECT 
    g.name AS genre, 
    COUNT(tg.show_id) AS number_of_shows
FROM 
    tv_genres g
JOIN 
    tv_show_genres tg ON g.id = tg.genre_id
GROUP BY 
    g.name
HAVING 
    COUNT(tg.show_id) > 0
ORDER BY 
    number_of_shows DESC;