-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
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