SELECT b.ingredient_type, SUM(a.total_order) as total_order
FROM first_half as a
    INNER JOIN icecream_info as b
    ON a.flavor = b.flavor
GROUP BY b.ingredient_type
ORDER BY total_order ASC