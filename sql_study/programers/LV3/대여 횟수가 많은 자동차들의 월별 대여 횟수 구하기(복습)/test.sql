-- 코드를 입력하세요
SELECT MONTH(START_DATE) as MONTH, CAR_ID, COUNT(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' and '2022-10'
 AND CAR_ID in 
 (select CAR_ID
 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
  where DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' and '2022-10'
 group by CAR_ID
 HAVING COUNT(CAR_ID) >= 5)

GROUP BY CAR_ID, MONTH(START_DATE)
HAVING RECORDS >= 1
ORDER BY MONTH ASC, CAR_ID DESC