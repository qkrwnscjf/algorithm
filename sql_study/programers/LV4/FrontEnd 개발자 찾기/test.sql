-- 코드를 작성해주세요
-- 1. CTE X
SELECT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
WHERE
    SKILL_CODE & ( -- & 연산자 : 각 정수형 값을 이진수로 변환하여 비교분석(and의 개념), join 연산시에도 사용이 가능하다.
        SELECT SUM(CODE)
        FROM SKILLCODES
        WHERE CATEGORY = 'Front End'
    ) > 0
ORDER BY
    ID ASC;
    
    
WITH TBL AS (
    SELECT SUM(CODE) AS SUM_CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End')

SELECT
    d.ID,
    d.EMAIL,
    d.FIRST_NAME,
    d.LAST_NAME
FROM
    DEVELOPERS d INNER JOIN TBL t
    ON d.SKILL_CODE & t.SUM_CODE > 0
ORDER BY
     d.ID ASC;