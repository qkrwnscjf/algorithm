# 2022년 3월 오프라인/온라인 상품 판매 내역 조회

## 문제 설명

의류 쇼핑몰의 온라인 및 오프라인 판매 데이터를 담고 있는 `ONLINE_SALE`, `OFFLINE_SALE` 테이블이 있습니다.

### ONLINE_SALE 테이블

| Column Name     | Type     | Nullable | 설명                     |
|------------------|----------|----------|--------------------------|
| ONLINE_SALE_ID   | INTEGER  | FALSE    | 온라인 판매 고유 ID       |
| USER_ID          | INTEGER  | FALSE    | 구매한 회원의 ID          |
| PRODUCT_ID       | INTEGER  | FALSE    | 판매된 상품의 ID          |
| SALES_AMOUNT     | INTEGER  | FALSE    | 판매량                    |
| SALES_DATE       | DATE     | FALSE    | 판매일                    |

- 동일한 날짜, 회원 ID, 상품 ID 조합에 대해 **중복된 데이터는 존재하지 않습니다.**

### OFFLINE_SALE 테이블

| Column Name     | Type     | Nullable | 설명                     |
|------------------|----------|----------|--------------------------|
| OFFLINE_SALE_ID  | INTEGER  | FALSE    | 오프라인 판매 고유 ID     |
| PRODUCT_ID       | INTEGER  | FALSE    | 판매된 상품의 ID          |
| SALES_AMOUNT     | INTEGER  | FALSE    | 판매량                    |
| SALES_DATE       | DATE     | FALSE    | 판매일                    |

- 동일한 날짜, 상품 ID 조합에 대해 **중복된 데이터는 존재하지 않습니다.**

## 목표

- `ONLINE_SALE`과 `OFFLINE_SALE` 테이블에서 **2022년 3월**에 발생한 판매 데이터를 추출합니다.
- `OFFLINE_SALE` 테이블에서 조회한 데이터는 `USER_ID`를 `NULL`로 표시합니다.
- 출력 항목:
  - `SALES_DATE`: 판매일
  - `PRODUCT_ID`: 상품 ID
  - `USER_ID`: 회원 ID (오프라인의 경우 `NULL`)
  - `SALES_AMOUNT`: 판매량
- 정렬 기준:
  1. `SALES_DATE` 오름차순
  2. `PRODUCT_ID` 오름차순
  3. `USER_ID` 오름차순

## 예시 데이터

### ONLINE_SALE

| ONLINE_SALE_ID | USER_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE  |
|----------------|---------|------------|---------------|--------------|
| 1              | 1       | 3          | 2             | 2022-02-25   |
| 2              | 4       | 4          | 1             | 2022-03-01   |
| 4              | 2       | 2          | 2             | 2022-03-02   |
| 3              | 6       | 3          | 3             | 2022-03-02   |
| 5              | 5       | 5          | 1             | 2022-03-03   |
| 6              | 5       | 7          | 1             | 2022-04-06   |

### OFFLINE_SALE

| OFFLINE_SALE_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE  |
|------------------|------------|---------------|--------------|
| 1                | 1          | 2             | 2022-02-21   |
| 4                | 1          | 2             | 2022-03-01   |
| 3                | 3          | 3             | 2022-03-01   |
| 2                | 4          | 1             | 2022-03-01   |
| 5                | 2          | 1             | 2022-03-03   |
| 6                | 2          | 1             | 2022-04-01   |

## 출력 결과 예시

| SALES_DATE | PRODUCT_ID | USER_ID | SALES_AMOUNT |
|------------|------------|---------|---------------|
| 2022-03-01 | 1          | NULL    | 2             |
| 2022-03-01 | 3          | NULL    | 3             |
| 2022-03-01 | 4          | NULL    | 1             |
| 2022-03-01 | 4          | 4       | 1             |
| 2022-03-02 | 2          | 2       | 2             |
| 2022-03-02 | 3          | 6       | 3             |
| 2022-03-03 | 2          | NULL    | 1             |
| 2022-03-03 | 5          | 5       | 1             |
