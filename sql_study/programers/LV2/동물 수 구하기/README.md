# 🐾 보호소에 들어온 전체 동물 수 구하기

## 📌 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물들의 정보를 담고 있습니다.  
이 테이블에서 **보호소에 들어온 전체 동물의 수**를 구하세요.

---

## 🗃️ 테이블 구조

### ANIMAL_INS

| 컬럼명            | 타입       | NULL 여부 | 설명                    |
|------------------|------------|-----------|-------------------------|
| ANIMAL_ID        | VARCHAR(N) | FALSE     | 동물의 고유 ID          |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE     | 동물의 종 (예: Dog, Cat) |
| DATETIME         | DATETIME   | FALSE     | 보호소에 들어온 날짜     |
| INTAKE_CONDITION | VARCHAR(N) | FALSE     | 입소 당시 상태           |
| NAME             | VARCHAR(N) | TRUE      | 동물의 이름             |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE     | 성별 및 중성화 여부     |

---

## ✅ 출력 조건

- 보호소에 들어온 전체 동물의 수를 출력합니다.
- 단순히 전체 레코드 수를 세면 됩니다 (`COUNT(*)` 사용).

> 출력 컬럼명은 문제에서 제시된 `count`와 달라도 무방합니다.

---

## 💡 예시

### 입력 데이터 예시

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE  |
|-----------|--------------|---------------------|------------------|----------|------------------|
| A399552   | Dog          | 2013-10-14 15:38:00 | Normal           | Jack     | Neutered Male    |
| A379998   | Dog          | 2013-10-23 11:42:00 | Normal           | Disciple | Intact Male      |
| A370852   | Dog          | 2013-11-03 15:04:00 | Normal           | Katie    | Spayed Female    |
| A403564   | Dog          | 2013-11-18 17:03:00 | Normal           | Anna     | Spayed Female    |

### 출력 예시

| count |
|-------|
| 4     |

- 총 4마리의 동물이 보호소에 입소함

---

## 🧠 SQL 풀이 힌트

```sql
SELECT COUNT(*)
FROM ANIMAL_INS;
