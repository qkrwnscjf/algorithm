# ROOT 아이템 조회 문제

## 📌 문제 설명

해당 게임에서 아이템들은 업그레이드가 가능한 구조로 구성되어 있습니다.  
아이템 간의 관계는 다음과 같습니다:

- `ITEM_A → ITEM_B` 형태의 업그레이드가 있을 때,  
  - `ITEM_A`는 `ITEM_B`의 **PARENT 아이템**
  - **PARENT 아이템이 없는 경우** → **ROOT 아이템**이라고 정의됩니다.

---

## 🗂 테이블 구조

### ITEM_INFO

| 컬럼명    | 타입       | NULL 허용 | 설명           |
|-----------|------------|-----------|----------------|
| ITEM_ID   | INTEGER    | FALSE     | 아이템 ID      |
| ITEM_NAME | VARCHAR(N) | FALSE     | 아이템 이름    |
| RARITY    | VARCHAR(N) | FALSE     | 아이템 희귀도  |
| PRICE     | INTEGER    | FALSE     | 아이템 가격    |

---

### ITEM_TREE

| 컬럼명          | 타입     | NULL 허용 | 설명                         |
|------------------|----------|-----------|------------------------------|
| ITEM_ID          | INTEGER  | FALSE     | 아이템 ID                    |
| PARENT_ITEM_ID   | INTEGER  | TRUE      | PARENT 아이템 ID (ROOT는 NULL) |

- 각 아이템은 하나의 PARENT만 가질 수 있으며,  
  **ROOT 아이템**은 `PARENT_ITEM_ID`가 `NULL`입니다.

---

## ❓ 문제 요구사항

- `ROOT 아이템`을 찾아 다음 정보를 출력하는 SQL문을 작성하세요:
  - `ITEM_ID`
  - `ITEM_NAME`
- 결과는 `ITEM_ID`를 기준으로 **오름차순** 정렬합니다.

---

## 💡 예시

### ITEM_INFO 테이블

| ITEM_ID | ITEM_NAME | RARITY | PRICE  |
|---------|-----------|--------|--------|
| 0       | ITEM_A    | COMMON | 10000  |
| 1       | ITEM_B    | LEGEND | 9000   |
| 2       | ITEM_C    | LEGEND | 11000  |
| 3       | ITEM_D    | UNIQUE | 10000  |
| 4       | ITEM_E    | LEGEND | 12000  |

### ITEM_TREE 테이블

| ITEM_ID | PARENT_ITEM_ID |
|---------|----------------|
| 0       | NULL           |
| 1       | 0              |
| 2       | 0              |
| 3       | NULL           |
| 4       | 3              |

---

### 🔍 분석

- ROOT 아이템: `ITEM_ID`가 `0`, `3`인 아이템 (`PARENT_ITEM_ID IS NULL`)
- 따라서 결과는 다음과 같아야 합니다:

---

## ✅ 출력 예시

| ITEM_ID | ITEM_NAME |
|---------|-----------|
| 0       | ITEM_A    |
| 3       | ITEM_D    |
