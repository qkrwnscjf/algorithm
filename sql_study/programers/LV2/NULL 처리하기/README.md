# 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물들의 정보를 담고 있습니다.  
테이블의 주요 컬럼은 다음과 같습니다:

| 컬럼명           | 타입      | 설명                     |
| ---------------- | --------- | ------------------------ |
| ANIMAL_ID        | VARCHAR   | 동물 고유 아이디         |
| ANIMAL_TYPE      | VARCHAR   | 동물 종류                |
| DATETIME         | DATETIME  | 보호 시작 시각           |
| INTAKE_CONDITION | VARCHAR   | 보호 시작 시 상태        |
| NAME             | VARCHAR   | 동물 이름 (NULL 가능)    |
| SEX_UPON_INTAKE  | VARCHAR   | 성별 및 중성화 여부      |

---

# 문제

입양 게시판에 정보를 게시하기 위해  
**동물의 생물 종, 이름, 성별 및 중성화 여부**를 **아이디 오름차순**으로 조회하는 SQL문을 작성하세요.

- 단, `NAME` 컬럼이 `NULL`인 경우 `"No name"`으로 표시해야 합니다.

---

# 예시

`ANIMAL_INS` 테이블이 다음과 같을 경우:

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME  | SEX_UPON_INTAKE |
|-----------|--------------|---------------------|------------------|--------|-----------------|
| A350276   | Cat          | 2017-08-13 13:50:00 | Normal           | Jewel  | Spayed Female   |
| A350375   | Cat          | 2017-03-06 15:01:00 | Normal           | Meo    | Neutered Male   |
| A368930   | Dog          | 2014-06-08 13:20:00 | Normal           | NULL   | Spayed Female   |

결과는 다음과 같아야 합니다:

| ANIMAL_TYPE | NAME     | SEX_UPON_INTAKE |
|-------------|----------|-----------------|
| Cat         | Jewel    | Spayed Female   |
| Cat         | Meo      | Neutered Male   |
| Dog         | No name  | Spayed Female   |

---

# 참고

- `NULL` 값을 `"No name"`으로 대체하기 위해 `IFNULL()` 또는 `COALESCE()` 함수 등을 사용할 수 있습니다.
- 본 문제는 Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes" 데이터셋을 기반으로 하며, ODbL(Open Database License)의 적용을 받습니다.
