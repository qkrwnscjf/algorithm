# 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물들의 정보를 담고 있습니다.  
테이블의 주요 컬럼은 다음과 같습니다:

| 컬럼명          | 타입      | 설명                     |
| --------------- | --------- | ------------------------ |
| ANIMAL_ID       | VARCHAR   | 동물의 고유 아이디       |
| ANIMAL_TYPE     | VARCHAR   | 동물 종류                |
| DATETIME        | DATETIME  | 보호소에 들어온 날짜 및 시간 |
| INTAKE_CONDITION| VARCHAR   | 들어왔을 때 상태          |
| NAME            | VARCHAR   | 동물 이름 (NULL 가능)    |
| SEX_UPON_INTAKE | VARCHAR   | 성별 및 중성화 여부       |

---

# 문제

`ANIMAL_INS` 테이블에서 모든 동물의 `ANIMAL_ID`, `NAME`, 그리고 보호소에 들어온 날짜(시각 제외)를 조회하는 SQL 문을 작성하세요.  
결과는 `ANIMAL_ID` 순으로 오름차순 정렬되어야 합니다.

---

# 조건

- `DATETIME` 컬럼에서 날짜 부분만 출력합니다 (`YYYY-MM-DD` 형식).
- 시각(시:분:초)은 제외합니다.

---

# 예시

| ANIMAL_ID | NAME   | 날짜        |
| --------- | ------ | ----------- |
| A349996   | Sugar  | 2018-01-22  |
| A350276   | Jewel  | 2017-08-13  |
| A350375   | Meo    | 2017-03-06  |
| A352555   | Harley | 2014-08-08  |
| A352713   | Gia    | 2017-04-13  |

---

# 참고

본 문제는 Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes" 데이터셋을 기반으로 하며, ODbL(Open Database License)의 적용을 받습니다.
