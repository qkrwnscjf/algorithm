-- 코드를 작성해주세요
SELECT
    ITEM_ID,
    ITEM_NAME,
    RARITY
FROM ITEM_INFO
WHERE ITEM_ID NOT IN (SELECT DISTINCT PARENT_ITEM_ID
                      FROM ITEM_TREE
                      WHERE PARENT_ITEM_ID IS NOT NULL)
ORDER BY ITEM_ID DESC;

----------------------------------------------------------
SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO A
WHERE NOT EXISTS (SELECT *
                     FROM ITEM_TREE B
                     WHERE B.PARENT_ITEM_ID = A.ITEM_ID )
ORDER BY ITEM_ID DESC;