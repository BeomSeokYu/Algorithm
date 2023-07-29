SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d')
FROM book
WHERE DATE_FORMAT(published_date, "%y") = '21' AND category = '인문'
ORDER BY published_date ASC