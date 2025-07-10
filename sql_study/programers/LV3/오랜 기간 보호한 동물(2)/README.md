# 🐾 보호 기간이 가장 길었던 입양 동물 조회

## 📄 테이블 정보

### ANIMAL_INS

| Column Name        | Type       | Nullable | Description                  |
|--------------------|------------|----------|------------------------------|
| ANIMAL_ID          | VARCHAR(N) | FALSE    | 동물 ID                      |
| ANIMAL_TYPE        | VARCHAR(N) | FALSE    | 동물 종류 (예: Dog, Cat)    |
| DATETIME           | DATETIME   | FALSE    | 보호 시작일                 |
| INTAKE_CONDITION   | VARCHAR(N) | FALSE    | 입소 시 상태                |
| NAME               | VARCHAR(N) | TRUE     | 이름                         |
| SEX_UPON_INTAKE    | VARCHAR(N) | FALSE    | 입소 시 성별/중성화 여부    |

### ANIMAL_OUTS

| Column Name        | Type       | Nullable | Description                  |
|--------------------|------------|----------|------------------------------|
| ANIMAL_ID          | VARCHAR(N) | FALSE    | 동물 ID (ANIMAL_INS 참조)   |
| ANIMAL_TYPE        | VARCHAR(N) | FALSE    | 동물 종류                   |
| DATETIME           | DATETIME   | FALSE    | 입양일                      |
| NAME               | VARCHAR(N) | TRUE     | 이름                         |
| SEX_UPON_OUTCOME   | VARCHAR(N) | FALSE    | 입양 시 성별/중성화 여부    |

---

## ❓ 문제 설명

입양을 간 동물 중 **보호소에 가장 오래 있었던 동물 2마리**의 ID와 이름을 조회하세요.

### ✅ 요구사항

- `입양일 - 보호 시작일` = 보호 기간
- 보호 기간이 **가장 긴 순서로 2마리**만 조회
- 출력 컬럼: `ANIMAL_ID`, `NAME`

---

## 💡 예시 결과

| ANIMAL_ID | NAME        |
|-----------|-------------|
| A362707   | Girly Girl  |
| A370507   | Emily       |

---

## 🧾 정답 SQL

```sql
SELECT
  I.ANIMAL_ID,
  I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
  ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2;
