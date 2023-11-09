SELECT ugu.user_id, ugu.nickname, SUM(ugb.price) as total_sales
FROM used_goods_board as ugb, used_goods_user as ugu
WHERE ugb.writer_id = ugu.user_id
    AND ugb.status = 'DONE'
GROUP BY ugu.user_id
HAVING total_sales >= 700000
ORDER BY total_sales ASC