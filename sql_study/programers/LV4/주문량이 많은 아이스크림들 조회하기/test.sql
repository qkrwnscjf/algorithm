-- 코드를 입력하세요
SELECT f.FLAVOR
FROM FIRST_HALF f 
JOIN JULY j on f.FLAVOR = j.FLAVOR
GROUP BY f.FLAVOR
ORDER BY SUM(f.TOTAL_ORDER) + SUM(j.TOTAL_ORDER) DESC
LIMIT 3