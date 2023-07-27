SELECT car_type, COUNT(car_type) as cars
FROM CAR_RENTAL_COMPANY_CAR
WHERE options LIKE ('%통풍시트%')
    OR options LIKE ('%열선시트%')
    OR options LIKE ('%가죽시트%')
GROUP BY car_type
ORDER BY car_type ASC