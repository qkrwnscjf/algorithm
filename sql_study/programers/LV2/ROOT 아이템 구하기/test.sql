-- 코드를 작성해주세요
select a.ITEM_ID, a.ITEM_NAME
from ITEM_INFO as a
join ITEM_TREE as b on a.item_id = b.item_id
where b.parent_item_id is null
order by a.ITEM_ID