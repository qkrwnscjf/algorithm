-- 코드를 작성해주세요
SELECT ID, LENGTH
FROM (
    SELECT ID, LENGTH,
           RANK() OVER (ORDER BY LENGTH DESC, ID ASC) as ranked
    FROM FISH_INFO
) 
WHERE ranked <= 10
