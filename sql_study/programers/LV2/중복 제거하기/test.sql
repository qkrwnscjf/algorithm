-- 코드를 입력하세요 : DISTINCT
SELECT COUNT(DISTINCT NAME) -- DISTINCT : null 제거
FROM ANIMAL_INS;

-- 코드를 입력하세요 : 서브 쿼리
SELECT COUNT(*)
FROM (select *
     from animal_ins
     where NAME is not null
     group by name) as animal_ins