SELECT flavor
FROM (
    SELECT fh.flavor, ingredient_type, total_order
    FROM first_half as fh JOIN icecream_info as iif
        ON fh.flavor = iif.flavor
    ) as temp
WHERE total_order > 3000 AND ingredient_type = 'fruit_based'
ORDER BY total_order DESC