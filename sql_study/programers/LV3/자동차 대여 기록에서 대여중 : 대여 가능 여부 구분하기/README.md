# 🚗 CAR_RENTAL_COMPANY_RENTAL_HISTORY: 대여 가능 여부 조회

## 📄 테이블 정보

### CAR_RENTAL_COMPANY_RENTAL_HISTORY

| Column Name | Type     | Nullable | Description     |
|-------------|----------|----------|-----------------|
| HISTORY_ID  | INTEGER  | FALSE    | 대여 기록 ID    |
| CAR_ID      | INTEGER  | FALSE    | 자동차 ID       |
| START_DATE  | DATE     | FALSE    | 대여 시작일     |
| END_DATE    | DATE     | FALSE    | 대여 종료일     |

---

## ❓ 문제 설명

자동차 대여 이력 테이블인 `CAR_RENTAL_COMPANY_RENTAL_HISTORY`에서  
**2022년 10월 16일**에 **대여 중인 자동차**를 파악하려고 합니다.

각 자동차별로 아래 조건에 따라 `AVAILABILITY` 상태를 확인하세요:

- `2022-10-16`이 `START_DATE`와 `END_DATE` 사이(포함)에 있으면 `"대여중"`
- 그렇지 않으면 `"대여 가능"`

### ✅ 요구사항

- 자동차 ID(`CAR_ID`)와 대여 여부(`AVAILABILITY`)를 조회
- 결과는 `CAR_ID` 기준으로 **내림차순 정렬**

---

## 💡 예시 출력

| CAR_ID | AVAILABILITY |
|--------|--------------|
| 4      | 대여중       |
| 3      | 대여 가능     |
| 2      | 대여중       |

---

