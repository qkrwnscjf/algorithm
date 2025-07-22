# 🛒 2022년 5월 식품 총매출 조회

## 📘 문제 설명

식품 정보와 주문 정보를 담고 있는 두 개의 테이블 **FOOD_PRODUCT**, **FOOD_ORDER**에서 **2022년 5월에 생산된 식품**에 대한 **총매출** 정보를 조회하려고 합니다.

총매출은 `가격 * 주문 수량`으로 계산되며, 다음 조건을 만족하는 SQL 문을 작성하세요:

- 2022년 5월(`2022-05-01` ~ `2022-05-31`) 생산된 식품만 조회
- `PRODUCT_ID`, `PRODUCT_NAME`, `TOTAL_SALES` 출력
- **총매출 내림차순**, 총매출이 같다면 **PRODUCT_ID 오름차순** 정렬

---

## 📂 테이블 정보

### FOOD_PRODUCT

| 컬럼명       | 타입           | 설명         |
|--------------|----------------|--------------|
| PRODUCT_ID   | VARCHAR(10)    | 식품 ID      |
| PRODUCT_NAME | VARCHAR(50)    | 식품 이름    |
| PRODUCT_CD   | VARCHAR(10)    | 식품 코드    |
| CATEGORY     | VARCHAR(10)    | 식품 분류    |
| PRICE        | NUMBER         | 식품 가격    |

### FOOD_ORDER

| 컬럼명       | 타입        | 설명         |
|--------------|-------------|--------------|
| ORDER_ID     | VARCHAR(10) | 주문 ID      |
| PRODUCT_ID   | VARCHAR(5)  | 식품 ID      |
| AMOUNT       | NUMBER      | 주문 수량    |
| PRODUCE_DATE | DATE        | 생산 일자    |
| IN_DATE      | DATE        | 입고 일자    |
| OUT_DATE     | DATE        | 출고 일자    |
| FACTORY_ID   | VARCHAR(10) | 공장 ID      |
| WAREHOUSE_ID | VARCHAR(10) | 창고 ID      |

---

## 💡 예시

### 🎯 FOOD_PRODUCT

| PRODUCT_ID | PRODUCT_NAME       | PRICE |
|------------|--------------------|-------|
| P0012      | 맛있는올리브유     | 7200  |
| P0014      | 맛있는마조유       | 8950  |
| P0017      | 맛있는들기름       | 7900  |
| P0019      | 맛있는카놀라유     | 5100  |

### 🎯 FOOD_ORDER

| ORDER_ID  | PRODUCT_ID | AMOUNT | PRODUCE_DATE |
|-----------|------------|--------|--------------|
| OD00000058 | P0017     | 1200   | 2022-05-19   |
| OD00000059 | P0017     | 1000   | 2022-05-24   |
| OD00000060 | P0019     | 2000   | 2022-05-29   |

---

### ✅ 출력 결과

| PRODUCT_ID | PRODUCT_NAME     | TOTAL_SALES |
|------------|------------------|-------------|
| P0017      | 맛있는들기름     | 17380000    |
| P0019      | 맛있는카놀라유   | 10200000    |

---

## ✅ SQL 문

```sql
SELECT
    FP.PRODUCT_ID,
    FP.PRODUCT_NAME,
    SUM(FO.AMOUNT * FP.PRICE) AS TOTAL_SALES
FROM FOOD_PRODUCT FP
JOIN FOOD_ORDER FO ON FP.PRODUCT_ID = FO.PRODUCT_ID
WHERE TO_CHAR(FO.PRODUCE_DATE, 'YYYY-MM') = '2022-05'
GROUP BY FP.PRODUCT_ID, FP.PRODUCT_NAME
ORDER BY TOTAL_SALES DESC, FP.PRODUCT_ID ASC;
