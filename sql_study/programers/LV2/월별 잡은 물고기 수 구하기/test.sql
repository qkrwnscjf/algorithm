-- 코드를 작성해주세요
select count(ID) as fish_count, MONTH(TIME) as month
from fish_info
group by MONTH(TIME)
order by month