SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d') as 'date_of_birth'
FROM member_profile
WHERE tlno IS NOT NULL
    AND date_of_birth LIKE '%-03-%'
    AND gender = 'W'
ORDER BY member_id ASC