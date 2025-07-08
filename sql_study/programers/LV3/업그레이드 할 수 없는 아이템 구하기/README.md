# 더 이상 업그레이드할 수 없는 아이템 조회

## 📘 문제 설명

게임 내에서 사용되는 아이템들은 업그레이드가 가능합니다.  
`ITEM_A` → `ITEM_B`와 같이 업그레이드가 가능할 때,  
- `ITEM_A`는 `ITEM_B`의 **PARENT 아이템**이며  
- **PARENT 아이템이 없는 경우**, 해당 아이템은 **ROOT 아이템**이라고 합니다.

### 📊 테이블 정보

#### `ITEM_INFO` - 아이템 기본 정보

| Column Name | Type         | Nullable | Description        |
|-------------|--------------|----------|--------------------|
| ITEM_ID     | INTEGER      | FALSE    | 아이템의 고유 ID   |
| ITEM_NAME   | VARCHAR(N)   | FALSE    | 아이템의 이름      |
| RARITY      | VARCHAR      | FALSE    | 아이템 희귀도      |
| PRICE       | INTEGER      | FALSE    | 아이템 가격        |

#### `ITEM_TREE` - 아이템 업그레이드 관계 정보

| Column Name       | Type    | Nullable | Description             |
|-------------------|---------|----------|-------------------------|
| ITEM_ID           | INTEGER | FALSE    | 아이템의 고유 ID        |
| PARENT_ITEM_ID    | INTEGER | TRUE     | 상위(PARENT) 아이템 ID  |

- `ITEM_TREE` 테이블은 각 아이템의 업그레이드 관계를 나타냅니다.
- `PARENT_ITEM_ID`가 `NULL`인 경우는 **ROOT 아이템**입니다.

> **보장 조건**
> - 각 아이템은 하나의 PARENT만 가집니다.
> - ROOT 아이템이 없는 경우는 없습니다.

---

## ✅ 문제 요구사항

더 이상 업그레이드할 수 없는 아이템을 조회하는 SQL문을 작성하세요.

### 출력 컬럼

| Column Name | Description         |
|-------------|---------------------|
| ITEM_ID     | 아이템의 고유 ID    |
| ITEM_NAME   | 아이템의 이름       |
| RARITY      | 아이템의 희귀도     |

### 조건
- 더 이상 업그레이드할 수 없는 아이템만 조회합니다.
  - 즉, 다른 아이템의 `PARENT_ITEM_ID`로 등장하지 않는 아이템
- 결과는 `ITEM_ID`를 기준으로 **내림차순 정렬**합니다.

---

## 🧪 예시

### ITEM_INFO

| ITEM_ID | ITEM_NAME | RARITY | PRICE |
|---------|-----------|--------|-------|
| 0       | ITEM_A    | RARE   | 10000 |
| 1       | ITEM_B    | RARE   | 9000  |
| 2       | ITEM_C    | LEGEND | 11000 |
| 3       | ITEM_D    | RARE   | 10000 |
| 4       | ITEM_E    | RARE   | 12000 |

### ITEM_TREE

| ITEM_ID | PARENT_ITEM_ID |
|---------|----------------|
| 0       | NULL           |
| 1       | 0              |
| 2       | 0              |
| 3       | 1              |
| 4       | 1              |

### 출력 예시

| ITEM_ID | ITEM_NAME | RARITY |
|---------|-----------|--------|
| 4       | ITEM_E    | RARE   |
| 3       | ITEM_D    | RARE   |
| 2       | ITEM_C    | LEGEND |

---

## 💡 풀이 핵심

- `ITEM_TREE`에서 `ITEM_ID`가 다른 행의 `PARENT_ITEM_ID`로 등장하지 않는 경우 해당 아이템은 업그레이드 대상이 아닙니다.
- 이를 `NOT EXISTS` 또는 `LEFT JOIN` + `WHERE NULL` 방식으로 판별할 수 있습니다.
