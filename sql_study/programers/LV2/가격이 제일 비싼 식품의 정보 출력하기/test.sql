-- sol 1
-- 서브쿼리 이용
SELECT *
from FOOD_PRODUCT
where price = (select max(price)
      from food_product
      )


-- sol 2
-- order by 이용
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1

-- sol 3
-- rank()

SELECT *
FROM (
    SELECT *, RANK() OVER (ORDER BY PRICE DESC) AS rnk
    FROM FOOD_PRODUCT
) AS ranked
WHERE rnk = 1;
