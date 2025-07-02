-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
#두 테이블 아이디 기준으로 결합
from BOOK as b
join AUTHOR as a on b.author_id = a.author_id
# 조건 설정('경제' 카테고리에 속하는 도서 아이디, 저자명 ,출판일 출력)
where b.category = '경제'
order by b.PUBLISHED_DATE