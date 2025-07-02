# 🧬 부모의 형질을 모두 보유한 대장균 찾기

## 📘 문제 설명

`ECOLI_DATA` 테이블은 실험실에서 배양한 대장균 개체들의 정보를 담고 있습니다. 각 행은 대장균 한 개체에 대한 정보를 나타내며, 테이블은 다음과 같은 구조를 가집니다:

| Column name             | Type     | Nullable | 설명                     |
|-------------------------|----------|----------|--------------------------|
| ID                      | INTEGER  | FALSE    | 대장균 개체의 ID         |
| PARENT_ID               | INTEGER  | TRUE     | 부모 개체의 ID (최초 개체는 NULL) |
| SIZE_OF_COLONY          | INTEGER  | FALSE    | 개체의 크기              |
| DIFFERENTIATION_DATE    | DATE     | FALSE    | 분화 날짜                |
| GENOTYPE                | INTEGER  | FALSE    | 개체의 형질 (2진수로 표현 가능) |

---

## 🧩 문제 목표

**부모의 형질을 모두 보유한 자식 대장균**을 찾아야 합니다. 결과는 다음과 같은 컬럼을 포함해야 합니다:

- 대장균의 ID (`ID`)
- 대장균의 형질 (`GENOTYPE`)
- 부모 대장균의 형질 (`PARENT_GENOTYPE`)

결과는 `ID` 기준으로 오름차순 정렬되어야 합니다.

---

