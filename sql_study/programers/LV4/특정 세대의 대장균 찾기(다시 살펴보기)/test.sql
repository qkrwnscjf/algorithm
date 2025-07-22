-- 코드를 작성해주세요
SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN ( 
    SELECT ID
    FROM ECOLI_DATA -- 2세대
    WHERE PARENT_ID IN (
        SELECT ID
        FROM ECOLI_DATA
        WHERE PARENT_ID IS NULL -- 1세대
    )
);

-- 재귀 함수인 WITH RECURSIVE, 자기 자신을 2번 JOIN도 있음.

SELECT c.ID
FROM ECOLI_DATA a
JOIN ECOLI_DATA b ON a.ID = b.PARENT_ID  -- a → b: 2세대
JOIN ECOLI_DATA c ON b.ID = c.PARENT_ID  -- b → c: 3세대
WHERE a.PARENT_ID IS NULL                -- a가 1세대

-- ----------------------------------------- --

WITH RECURSIVE generation_tree AS (
    SELECT
        ID,
        PARENT_ID,
        1 AS generation
    FROM
        ECOLI_DATA
    WHERE
        PARENT_ID IS NULL -- 1세대 (최초 부모)

    UNION ALL

    SELECT
        e.ID,
        e.PARENT_ID,
        g.generation + 1
    FROM
        ECOLI_DATA e
        JOIN generation_tree g ON e.PARENT_ID = g.ID
)
SELECT *
FROM generation_tree
WHERE generation = 3;
