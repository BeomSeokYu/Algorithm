SELECT HOUR(datetime) as hh, COUNT(datetime)
FROM animal_outs
GROUP BY hh
HAVING hh BETWEEN 9 AND 19
ORDER BY hh