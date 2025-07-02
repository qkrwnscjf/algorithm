# 아이스크림 성분 타입별 상반기 총주문량 조회

## 📄 문제 설명

아래 두 개의 테이블을 활용하여 상반기 동안 아이스크림의 **성분 타입별 총주문량**을 구하는 SQL 문제입니다.

### 🍨 FIRST_HALF 테이블

| Column name   | Type       | Nullable | Description                                  |
|----------------|------------|----------|----------------------------------------------|
| SHIPMENT_ID    | INT(N)     | FALSE    | 출하 번호                                     |
| FLAVOR         | VARCHAR(N) | FALSE    | 아이스크림 맛 (기본 키)                      |
| TOTAL_ORDER    | INT(N)     | FALSE    | 상반기 총주문량                              |

### 🧾 ICECREAM_INFO 테이블

| Column name      | Type       | Nullable | Description                                 |
|------------------|------------|----------|---------------------------------------------|
| FLAVOR           | VARCHAR(N) | FALSE    | 아이스크림 맛 (기본 키)                     |
| INGREDIENT_TYPE  | VARCHAR(N) | FALSE    | 성분 타입 (sugar_based, fruit_based 등)     |

## ✅ 문제

- **상반기 동안** 각 아이스크림의 **성분 타입(INGREDIENT_TYPE)** 별로 아이스크림의 **총주문량(TOTAL_ORDER)** 을 구하세요.
- 결과는 총주문량을 기준으로 **오름차순 정렬**해야 합니다.
- 총주문량 컬럼명은 `TOTAL_ORDER`로 출력되어야 합니다.

## 💡 예시

### 📘 FIRST_HALF 테이블

| SHIPMENT_ID | FLAVOR           | TOTAL_ORDER |
|-------------|------------------|-------------|
| 101         | chocolate         | 3200        |
| 102         | vanilla           | 2800        |
| 103         | mint_chocolate    | 1700        |
| 104         | caramel           | 2600        |
| 105         | white_chocolate   | 3100        |
| 106         | peach             | 2450        |
| 107         | watermelon        | 2150        |
| 108         | mango             | 2900        |
| 109         | strawberry        | 3100        |
| 110         | melon             | 3150        |
| 111         | orange            | 2900        |
| 112         | pineapple         | 2900        |

### 📗 ICECREAM_INFO 테이블

| FLAVOR           | INGREDIENT_TYPE |
|------------------|------------------|
| chocolate         | sugar_based      |
| vanilla           | sugar_based      |
| mint_chocolate    | sugar_based      |
| caramel           | sugar_based      |
| white_chocolate   | sugar_based      |
| peach             | fruit_based      |
| watermelon        | fruit_based      |
| mango             | fruit_based      |
| strawberry        | fruit_based      |
| melon             | fruit_based      |
| orange            | fruit_based      |
| pineapple         | fruit_based      |

### 🔍 출력 결과

| INGREDIENT_TYPE | TOTAL_ORDER |
|------------------|--------------|
| sugar_based      | 13400        |
| fruit_based      | 19550        |

> 📌 참고: `FLAVOR` 컬럼은 두 테이블 간 조인을 위한 키이며, `FIRST_HALF.FLAVOR`는 `ICECREAM_INFO.FLAVOR`의 외래 키입니다.
