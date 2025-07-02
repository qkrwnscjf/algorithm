-- 코드를 입력하세요
#SELECT MCDP_CD as '진료과코드', count(*) as '5월예약건수'
#from appointment
#where YEAR(APNT_YMD) = 2022 and MONTH(APNT_YMD) = 5
#group by MCDP_CD
#order by '5월예약건수', '진료과코드'

SELECT MCDP_CD AS "진료과 코드",
       COUNT(*) AS "5월예약건수"
  FROM APPOINTMENT
 WHERE YEAR(APNT_YMD) = 2022
   AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY COUNT(*) ASC, MCDP_CD ASC; # order by는 실제 컬럼명을 적어야함.