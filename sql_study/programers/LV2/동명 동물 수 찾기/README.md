# 🐾 중복된 동물 이름 조회

## 📋 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담고 있습니다.  
각 컬럼의 의미는 다음과 같습니다:

| 컬럼명             | 타입         | NULL 허용 | 설명                     |
|------------------|--------------|-----------|------------------------|
| ANIMAL_ID        | VARCHAR(N)   | FALSE     | 동물의 아이디              |
| ANIMAL_TYPE      | VARCHAR(N)   | FALSE     | 동물의 생물 종             |
| DATETIME         | DATETIME     | FALSE     | 보호 시작일                |
| INTAKE_CONDITION | VARCHAR(N)   | FALSE     | 보호 시작 시 상태           |
| NAME             | VARCHAR(N)   | TRUE      | 동물의 이름                |
| SEX_UPON_INTAKE  | VARCHAR(N)   | FALSE     | 성별 및 중성화 여부          |

동물 보호소에 들어온 동물 이름 중, **두 번 이상 사용된 이름**과 **해당 이름이 사용된 횟수**를 조회하는 SQL 문을 작성해주세요.

단, 다음 조건을 만족해야 합니다:
- 이름이 없는 동물(`NAME IS NULL`)은 집계에서 제외
- 결과는 이름(`NAME`) 기준 오름차순으로 정렬

---

## 💡 예시

예를 들어, `ANIMAL_INS` 테이블이 다음과 같다면:

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
|-----------|-------------|---------------------|------------------|--------|-----------------|
| A396810   | Dog         | 2016-08-22 16:13:00 | Injured          | Raven  | Spayed Female   |
| A377750   | Dog         | 2017-10-25 17:17:00 | Normal           | Lucy   | Spayed Female   |
| A355688   | Dog         | 2014-01-26 13:48:00 | Normal           | Shadow | Neutered Male   |
| A399421   | Dog         | 2015-08-25 14:08:00 | Normal           | Lucy   | Spayed Female   |
| A400680   | Dog         | 2017-06-17 13:29:00 | Normal           | Lucy   | Spayed Female   |
| A410668   | Cat         | 2015-11-19 13:41:00 | Normal           | Raven  | Spayed Female   |

중복 이름:
- `Lucy`는 3번 사용됨
- `Raven`은 2번 사용됨

따라서, 쿼리 실행 결과는 다음과 같아야 합니다:

| NAME  | COUNT |
|-------|-------|
| Lucy  | 3     |
| Raven | 2     |

---

## 📂 데이터 출처

본 문제는 Kaggle의  
["Austin Animal Center Shelter Intakes and Outcomes"](https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)  
데이터를 기반으로 하며, ODbL의 적용을 받습니다.
