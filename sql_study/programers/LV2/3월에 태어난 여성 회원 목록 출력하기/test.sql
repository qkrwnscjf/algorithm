-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH -- DATE_FORMAT으로 날짜 변경(%y시 대소문자에따라 결과 다름)
from MEMBER_PROFILE
where GENDER = 'W' and MONTH(DATE_OF_BIRTH) = '3' and TLNO is not null
order by MEMBER_ID asc