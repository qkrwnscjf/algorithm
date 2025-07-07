-- 코드를 입력하세요
SELECT CAR_ID, ROUND(AVG(TIMESTAMPDIFF(DAY, START_DATE, END_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;

-- DATEDIFF vs TIMESTAMPDIFF: 날짜 차이를 계산하는 두 가지 방법
MySQL에서 날짜나 시간 간의 차이를 계산할 때 자주 사용하는 함수로는 DATEDIFF와 TIMESTAMPDIFF가 있습니다. 이 두 함수는 비슷한 목적을 가지고 있지만, 사용법과 반환 값에서 차이가 있습니다.

1. DATEDIFF
DATEDIFF는 두 날짜 간의 일 단위 차이를 계산하는 간단한 함수입니다. 시간 부분은 무시되며, 오직 날짜만을 비교합니다. 반환 값은 두 날짜 사이의 일 수입니다.

DATEDIFF('2024-08-01', '2024-07-25'); 
# 7
2. TIMESTAMPDIFF
TIMESTAMPDIFF는 두 날짜 또는 시간 간의 차이를 특정 단위(년, 월, 일, 시 등)로 계산할 수 있는 좀 더 유연한 함수입니다. 첫 번째 인자로 비교 단위를 지정할 수 있어, 보다 다양한 비교가 가능합니다.

TIMESTAMPDIFF(DAY, '2024-08-01 10:00:00', '2024-07-25 15:30:00');
# 7

TIMESTAMPDIFF(HOUR, '2024-08-01 10:00:00', '2024-07-25 15:30:00')
# 186
