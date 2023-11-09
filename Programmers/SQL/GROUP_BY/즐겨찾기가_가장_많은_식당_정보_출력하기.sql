SELECT a.food_type, a.rest_id, a.rest_name, a.favorites
FROM rest_info as a
    JOIN (  SELECT food_type, MAX(favorites) as favorites
            FROM rest_info
            GROUP BY food_type ) as b
    ON a.food_type = b.food_type AND a.favorites = b.favorites
ORDER BY food_type DESC