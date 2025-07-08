
-- 2022년 1월에 판매된 책들의 카테고리별 총 판매 건수
SELECT a.category, sum(b.sales) AS total_sales
FROM book a
JOIN book_sales b ON a.book_id = b.book_id
WHERE YEAR(b.sales_date) = 2022 AND MONTH(b.sales_date) = 1
GROUP BY a.category
order by a.category

-- where : 그룹 집계 전 필터링(그룹과 관련 없는 연산이 필요한 경우)
-- having : 그룹화 후 필터링(그룹내 계산이 필요할 시 사용)