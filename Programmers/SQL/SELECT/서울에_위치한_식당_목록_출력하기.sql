SELECT rest_id , rest_name, food_type, favorites, address, FORMAT(AVG(review_score), 2) as score
FROM (
    SELECT ri.rest_id , rest_name, food_type, favorites, address, review_score
    FROM rest_info as ri RIGHT JOIN rest_review as rr ON ri.rest_id = rr.rest_id
    WHERE address LIKE '서울%'
) as tt
GROUP BY rest_id
ORDER BY score DESC, favorites DESC