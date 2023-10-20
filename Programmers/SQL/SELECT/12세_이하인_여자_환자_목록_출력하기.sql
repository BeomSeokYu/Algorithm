SELECT pt_name, pt_no, gend_cd, age, IFNULL(tlno, 'NONE') as tlno
FROM PATIENT
WHERE age < 13 AND GEND_CD = 'W'
ORDER BY age DESC, pt_name ASC