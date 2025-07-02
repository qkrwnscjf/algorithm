# ITEM_INFO - LEGEND 아이템 총 가격 조회

## 📘 개요

본 프로젝트는 게임 아이템 정보를 담고 있는 `ITEM_INFO` 테이블을 기반으로, 희귀도(`RARITY`)가 `LEGEND`인 아이템들의 가격 총합을 구하는 SQL 쿼리를 작성하는 문제입니다.

---

## 🗃️ 테이블 구조

### ITEM_INFO

| Column Name | Type       | Nullable | Description       |
|-------------|------------|----------|-------------------|
| ITEM_ID     | INTEGER    | NOT NULL | 아이템 ID         |
| ITEM_NAME   | VARCHAR(N) | NOT NULL | 아이템 이름       |
| RARITY      | VARCHAR(N) | NOT NULL | 아이템 희귀도     |
| PRICE       | INTEGER    | NOT NULL | 아이템 가격 (₩)   |

---

## 🎯 문제

`ITEM_INFO` 테이블에서 `RARITY`가 `'LEGEND'`인 아이템들의 `PRICE` 총합을 계산하는 SQL 문을 작성하세요.

- 결과 컬럼의 이름은 반드시 `TOTAL_PRICE`로 지정해야 합니다.

---

## 📝 출력 예시

예를 들어 `ITEM_INFO` 테이블이 다음과 같을 경우:

| ITEM_ID | ITEM_NAME | RARITY | PRICE  |
|---------|-----------|--------|--------|
| 0       | ITEM_A    | COMMON | 10000  |
| 1       | ITEM_B    | LEGEND | 9000   |
| 2       | ITEM_C    | LEGEND | 11000  |
| 3       | ITEM_D    | UNIQUE | 10000  |
| 4       | ITEM_E    | LEGEND | 12000  |

조건에 해당하는 아이템 가격 총합은 다음과 같습니다:

| TOTAL_PRICE |
|-------------|
| 32000       |

---

## 💡 SQL 정답 예시

```sql
SELECT 
    SUM(PRICE) AS TOTAL_PRICE
FROM 
    ITEM_INFO
WHERE 
    RARITY = 'LEGEND';
