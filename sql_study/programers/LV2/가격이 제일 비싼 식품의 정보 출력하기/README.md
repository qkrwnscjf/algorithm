# 🥫 가장 비싼 식품 정보 조회 - SQL 문제

## 📝 문제 설명

`FOOD_PRODUCT` 테이블은 다양한 식품들의 정보를 담고 있으며, 각 식품의 ID, 이름, 코드, 분류, 가격 정보를 포함합니다.

이 문제에서는 가격(`PRICE`)이 **가장 비싼** 식품 1개의 전체 정보를 조회하는 SQL 쿼리를 작성해야 합니다.

---

## 🗃️ 테이블 구조

### `FOOD_PRODUCT`

| 컬럼명       | 타입         | NULL 허용 | 설명         |
|--------------|--------------|------------|--------------|
| PRODUCT_ID   | VARCHAR(10)  | FALSE      | 식품 ID      |
| PRODUCT_NAME | VARCHAR(50)  | FALSE      | 식품 이름    |
| PRODUCT_CD   | VARCHAR(10)  | TRUE       | 식품 코드    |
| CATEGORY     | VARCHAR(10)  | TRUE       | 식품 분류    |
| PRICE        | NUMBER       | TRUE       | 식품 가격    |

---

## ✅ 요구사항

- 가격이 **가장 높은** 식품 한 개를 조회
- 출력 컬럼: `PRODUCT_ID`, `PRODUCT_NAME`, `PRODUCT_CD`, `CATEGORY`, `PRICE`
- 동일한 가격의 식품이 여러 개일 경우, 전부 출력 (즉, **최댓값 필터링**)

---

## 💡 예시

### 입력 예시

| PRODUCT_ID | PRODUCT_NAME     | PRODUCT_CD  | CATEGORY | PRICE |
|------------|------------------|-------------|----------|-------|
| P0018      | 맛있는고추기름   | CD_OL00008  | 식용유   | 6100  |
| P0019      | 맛있는카놀라유   | CD_OL00009  | 식용유   | 5100  |
| P0020      | 맛있는산초유     | CD_OL00010  | 식용유   | 6500  |
| P0021      | 맛있는케첩       | CD_OL00001  | 소스     | 4500  |
| P0022      | 맛있는마요네즈   | CD_OL00002  | 소스     | 4700  |

### 출력 예시

| PRODUCT_ID | PRODUCT_NAME   | PRODUCT_CD  | CATEGORY | PRICE |
|------------|----------------|-------------|----------|-------|
| P0020      | 맛있는산초유   | CD_OL00010  | 식용유   | 6500  |

---

## 🧾 SQL 예시

```sql
SELECT 
    PRODUCT_ID, 
    PRODUCT_NAME, 
    PRODUCT_CD, 
    CATEGORY, 
    PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);
