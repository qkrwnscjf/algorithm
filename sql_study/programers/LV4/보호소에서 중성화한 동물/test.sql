-- 코드를 입력하세요
-- 중성화 X : intact , 중성화 O : Spayed, Neutered
-- 구하고자 : INS에서 중성화 X, OUT에서 중성화 O
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.SEX_UPON_INTAKE LIKE 'Intact%' and (o.SEX_UPON_OUTCOME LIKE 'Spayed%' or o.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY ANIMAL_ID