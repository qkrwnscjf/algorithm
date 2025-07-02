SELECT CAR_TYPE,
       COUNT(*) AS CARS
  FROM CAR_RENTAL_COMPANY_CAR
 WHERE OPTIONS LIKE '%통풍시트%'
    OR OPTIONS LIKE '%열선시트%' #options att가 다중 문자열로 구성이라 콤마(,) 구분이 어려움.
    OR OPTIONS LIKE '%가죽시트%'
 GROUP BY CAR_TYPE
 ORDER BY CAR_TYPE ASC;