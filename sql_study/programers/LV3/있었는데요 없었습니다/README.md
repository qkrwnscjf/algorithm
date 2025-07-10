# 🐾 보호 시작일보다 빠른 입양일 조회

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

일부 동물의 입양일(`ANIMAL_OUTS.DATETIME`)이 보호 시작일(`ANIMAL_INS.DATETIME`)보다 **빠르게 기록된 오류**가 있습니다.

📌 **입양일 < 보호 시작일** 인 동물들의 ID와 이름을 조회하세요.

### ✅ 요구사항

- 보호 시작일보다 입양일이 더 빠른 동물만 조회
- 결과는 보호 시작일 기준 **오름차순 정렬**
- 출력 컬럼: `ANIMAL_ID`, `NAME`

---

## 💡 예시 결과

| ANIMAL_ID | NAME     |
|-----------|----------|
| A381217   | Cherokee |

---

## 🧾 정답 SQL

```sql
SELECT
  I.ANIMAL_ID,
  I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O
  ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME < I.DATETIME
ORDER BY I.DATETIME;
