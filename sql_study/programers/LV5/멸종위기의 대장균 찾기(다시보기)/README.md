# 세대별 자식이 없는 대장균 개체 수 조회

## 문제 설명

`ECOLI_DATA` 테이블은 실험실에서 배양한 대장균들의 정보를 담고 있으며,  
개체의 고유 ID와 부모 ID를 통해 세대별 계보를 알 수 있습니다.

### ECOLI_DATA 테이블 구조

| Column name             | Type    | Nullable |
|-------------------------|---------|----------|
| ID                      | INTEGER | FALSE    |
| PARENT_ID               | INTEGER | TRUE     |
| SIZE_OF_COLONY          | INTEGER | FALSE    |
| DIFFERENTIATION_DATE    | DATE    | FALSE    |
| GENOTYPE                | INTEGER | FALSE    |

- 최초의 대장균 개체는 `PARENT_ID`가 NULL입니다.
- 자식 개체는 분화된 결과이며, `PARENT_ID`를 통해 부모 개체를 참조합니다.

---

## 문제

각 세대(GENERATION)별 **자식이 없는 개체의 수(COUNT)** 와  
**세대 번호(GENERATION)** 를 출력하는 SQL문을 작성해주세요.

조건:

- 결과는 `GENERATION` 기준으로 **오름차순 정렬**합니다.
- 모든 세대에는 자식이 없는 개체가 적어도 1개 존재합니다.

---

## 예시

예시 테이블: `ECOLI_DATA`

| ID  | PARENT_ID | SIZE_OF_COLONY | DIFFERENTIATION_DATE | GENOTYPE |
|-----|-----------|----------------|-----------------------|----------|
| 1   | NULL      | 10             | 2019/01/01            | 5        |
| 2   | NULL      | 2              | 2019/01/01            | 3        |
| 3   | 2         | 100            | 2020/01/01            | 4        |
| 4   | 2         | 16             | 2020/01/01            | 4        |
| 5   | 2         | 17             | 2020/01/01            | 6        |
| 6   | 4         | 101            | 2021/01/01            | 22       |
| 7   | 4         | 101            | 2022/01/01            | 23       |
| 8   | 6         | 1              | 2022/01/01            | 27       |

세대 구분:

- 1세대: ID 1, 2 (`PARENT_ID` = NULL)
- 2세대: ID 3, 4, 5 (부모: ID 2)
- 3세대: ID 6, 7 (부모: ID 4)
- 4세대: ID 8 (부모: ID 6)

자식이 없는 개체들:

- 1세대: ID 1
- 2세대: ID 3, 5
- 3세대: ID 7
- 4세대: ID 8

---

## 출력 결과

| COUNT | GENERATION |
|-------|------------|
| 1     | 1          |
| 2     | 2          |
| 1     | 3          |
| 1     | 4          |
