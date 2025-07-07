# 아이템 업그레이드 경로 탐색 문제

## 📌 문제 설명

해당 게임에서는 아이템이 업그레이드 되는 트리 구조를 가지고 있습니다.  
각 아이템은 하나의 PARENT 아이템을 가지며, 최상위 PARENT가 없는 아이템은 `ROOT 아이템`이라 합니다.  
예를 들어 `ITEM_A → ITEM_B → ITEM_C` 형태라면,  
- `ITEM_C`의 PARENT는 `ITEM_B`  
- `ITEM_B`의 PARENT는 `ITEM_A`  
- `ITEM_A`는 ROOT 아이템입니다.

---

## 🗂 테이블 구조

### ITEM_INFO

| 컬럼명    | 타입         | NULL 허용 | 설명           |
|-----------|--------------|-----------|----------------|
| ITEM_ID   | INTEGER      | FALSE     | 아이템 ID      |
| ITEM_NAME | VARCHAR(N)   | FALSE     | 아이템 이름    |
| RARITY    | VARCHAR(N)   | FALSE     | 아이템 희귀도  |
| PRICE     | INTEGER      | FALSE     | 아이템 가격    |

---

### ITEM_TREE

| 컬럼명          | 타입     | NULL 허용 | 설명                         |
|------------------|----------|-----------|------------------------------|
| ITEM_ID          | INTEGER  | FALSE     | 아이템 ID                    |
| PARENT_ITEM_ID   | INTEGER  | TRUE      | PARENT 아이템 ID (ROOT는 NULL) |

- 각 아이템은 오직 하나의 부모만 가질 수 있습니다.
- ROOT 아이템의 `PARENT_ITEM_ID`는 `NULL`입니다.
- ROOT가 없는 아이템은 존재하지 않습니다.

---

## ❓ 문제 요구사항

- 희귀도가 `'RARE'`인 아이템들의 **모든 다음 업그레이드 아이템**의  
  - `ITEM_ID`,  
  - `ITEM_NAME`,  
  - `RARITY`  
  를 출력하는 SQL을 작성하세요.

- 결과는 `ITEM_ID`를 기준으로 **내림차순** 정렬합니다.

---

## 💡 예시

### ITEM_INFO 테이블

| ITEM_ID | ITEM_NAME | RARITY | PRICE  |
|---------|-----------|--------|--------|
| 0       | ITEM_A    | RARE   | 10000  |
| 1       | ITEM_B    | RARE   | 9000   |
| 2       | ITEM_C    | LEGEND | 11000  |
| 3       | ITEM_D    | RARE   | 10000  |
| 4       | ITEM_E    | RARE   | 12000  |

### ITEM_TREE 테이블

| ITEM_ID | PARENT_ITEM_ID |
|---------|----------------|
| 0       | NULL           |
| 1       | 0              |
| 2       | 0              |
| 3       | 1              |
| 4       | 1              |

---

### 🔍 분석

- `RARE` 아이템: `ITEM_A`, `ITEM_B`, `ITEM_D`, `ITEM_E`
- 이 중 다음 업그레이드가 가능한 아이템:
