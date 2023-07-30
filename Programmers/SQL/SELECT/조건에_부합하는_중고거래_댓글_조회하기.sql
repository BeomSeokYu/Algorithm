SELECT title, ugb.board_id, reply_id, ugr.writer_id, ugr.contents, DATE_FORMAT(ugr.created_date, '%Y-%m-%d')
FROM used_goods_board as ugb INNER JOIN used_goods_reply as ugr
    ON ugb.board_id = ugr.board_id
WHERE DATE_FORMAT(ugb.created_date, '%Y-%m') = '2022-10'
ORDER BY ugr.created_date ASC, title ASC