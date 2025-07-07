-- 코드를 입력하세요
-- sol 1. case 구문 사용
SELECT ANIMAL_TYPE, 
    CASE
        WHEN NAME is null THEN 'No name'
        ELSE NAME
    END as 'NAME',
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- sol 2. IF NULL 사용
select animal_type, ifnull(name, 'No name') as 'name', sex_upon_intake
from animal_ins
order by animal_id asc;