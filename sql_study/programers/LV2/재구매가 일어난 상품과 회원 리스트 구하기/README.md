# 📦 의류 쇼핑몰 재구매 회원 및 상품 조회

## 📄 문제 설명

다음은 어느 의류 쇼핑몰의 온라인 상품 판매 정보를 담고 있는 **ONLINE_SALE** 테이블을 기반으로 하는 SQL 문제입니다.

### 🛒 ONLINE_SALE 테이블 구조

| Column name      | Type     | Nullable | Description                    |
|------------------|----------|----------|--------------------------------|
| ONLINE_SALE_ID   | INTEGER  | FALSE    | 온라인 상품 판매 ID            |
| USER_ID          | INTEGER  | FALSE    | 회원 ID                         |
| PRODUCT_ID       | INTEGER  | FALSE    | 상품 ID                         |
| SALES_AMOUNT     | INTEGER  | FALSE    | 판매량                          |
| SALES_DATE       | DATE     | FALSE    | 판매일                          |

> 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

---

## ✅ 문제

- 동일한 회원이 동일한 상품을 **2회 이상** 구매한 경우(재구매)를 조회합니다.
- 해당 재구매 이력이 있는 `USER_ID`, `PRODUCT_ID`를 출력합니다.
- 정렬 조건:
  - `USER_ID` 기준 **오름차순**
  - `PRODUCT_ID` 기준 **내림차순**

---

## 💡 예시

### 📘 ONLINE_SALE 테이블 예시

| ONLINE_SALE_ID | USER_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE |
|----------------|---------|------------|---------------|-------------|
| 1              | 1       | 3          | 2             | 2022-02-25  |
| 2              | 1       | 4          | 1             | 2022-03-01  |
| 4              | 2       | 4          | 2             | 2022-03-12  |
| 3              | 1       | 3          | 3             | 2022-03-31  |
| 5              | 3       | 5          | 1             | 2022-04-03  |
| 6              | 2       | 4          | 1             | 2022-04-06  |
| 2              | 1       | 4          | 2             | 2022-05-11  |

---

### 🔍 출력 결과

| USER_ID | PRODUCT_ID |
|---------|-------------|
| 1       | 4           |
| 1       | 3           |
| 2       | 4           |

---

> 📌 참고:
> - `GROUP BY USER_ID, PRODUCT_ID`를 사용하여 구매 횟수(`COUNT(*)`)를 구합니다.
> - 조건절에 `HAVING COUNT(*) >= 2`를 포함시켜 재구매 필터링을 수행합니다.
