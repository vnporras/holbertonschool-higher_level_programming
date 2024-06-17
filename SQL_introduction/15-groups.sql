-- 15. Number by score
SELECT
  score,
  COUNT(score) number
FROM second_table
GROUP BY score 
ORDER BY COUNT(score) DESC;