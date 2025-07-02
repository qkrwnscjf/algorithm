-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE as INGREDIENT_TYPE, sum(f.total_order) as TOTAL_ORDER
from first_half as f
join icecream_info as i on f.FLAVOR = i.FLAVOR
group by ingredient_type
order by total_order