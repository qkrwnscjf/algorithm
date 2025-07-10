# 식품 주문 출고 여부 조회

## 📄 테이블 정보

### FOOD_ORDER 테이블

| Column Name   | Type        | Nullable | Description   |
|---------------|-------------|----------|----------------|
| ORDER_ID      | VARCHAR(10) | FALSE    | 주문 ID         |
| PRODUCT_ID    | VARCHAR(5)  | FALSE    | 제품 ID         |
| AMOUNT        | NUMBER      | FALSE    | 주문 수량        |
| PRODUCE_DATE  | DATE        | TRUE     | 생산일자         |
| IN_DATE       | DATE        | TRUE     | 입고일자         |
| OUT_DATE      | DATE        | TRUE     | 출고일자         |
| FACTORY_ID    | VARCHAR(10) | FALSE    | 공장 ID         |
| WAREHOUSE_ID  | VARCHAR(10) | FALSE    | 창고 ID         |

## ❓ 문제

`FOOD_ORDER` 테이블에서 **2022년 5월 1일**을 기준으로  
주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을 작성해주세요.

출고여부는 다음 조건에 따라 구분됩니다:

- `2022년 5월 1일` 이전 또는 같은 날짜인 경우: **출고완료**
- `2022년 5월 2일` 이후인 경우: **출고대기**
- `OUT_DATE`가 `NULL`인 경우: **출고미정**

결과는 `ORDER_ID`를 기준으로 **오름차순 정렬**해야 합니다.

## ✅ 출력 예시

| ORDER_ID     | PRODUCT_ID | OUT_DATE   | 출고여부   |
|--------------|------------|------------|-------------|
| OD00000051   | P0002      | 2022-04-21 | 출고완료     |
| OD00000052   | P0003      | 2022-04-27 | 출고완료     |
| OD00000053   | P0005      | 2022-05-01 | 출고완료     |
| OD00000054   | P0006      |            | 출고미정     |
| OD00000055   | P0008      | 2022-05-11 | 출고대기     |

