-- 코드를 작성해주세요
select count(*) as fish_count , max(length) as max_length, fish_type
from fish_info
group by fish_type
having avg(IFNULL(length, 10)) >= 33
order by fish_type
-- group by 절 사용시 조건은 having으로, 그리고 그룹 문법 사용은 max, min, sum, avg등의 연산 select이 필수.(없으면 오류)
-- IFNULL사용 (변수, 값)