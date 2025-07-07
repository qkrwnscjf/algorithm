-- 코드를 작성해주세요
select a.item_id as ITEM_ID, a.ITEM_NAME as ITEM_NAME, a.RARITY as RARITY
from item_info a
join item_tree b on a.item_id = b.item_id
where b.parent_item_id in (
    select ITEM_ID
    from ITEM_INFO
    where RARITY = 'RARE' -- IN 사용시 b.~ = a.~ 형태 X ->서브쿼리나 특정 값을 지정해야함 EX. 지금 쿼리문처럼 혹은 ('100', '200') 이런거
)
order by a.ITEM_ID desc