# 문제 설명

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물들의 정보를 담고 있습니다.  
테이블 주요 컬럼은 다음과 같습니다:

| 컬럼명           | 타입      | 설명                   |
| ---------------- | --------- | ---------------------- |
| ANIMAL_ID        | VARCHAR   | 동물 고유 아이디       |
| ANIMAL_TYPE      | VARCHAR   | 동물 종류              |
| DATETIME         | DATETIME  | 입양 발생 날짜 및 시간 |
| NAME             | VARCHAR   | 동물 이름 (NULL 가능)  |
| SEX_UPON_OUTCOME | VARCHAR   | 성별 및 중성화 여부    |

---

# 문제

09:00부터 19:59까지 각 시간대별로 입양이 발생한 건수를 조회하는 SQL문을 작성하세요.

- 시간은 `DATETIME` 컬럼에서 추출하며, 시간 단위(HOUR)별로 집계합니다.
- 결과는 시간 순(HOUR 오름차순)으로 정렬해야 합니다.

---

# 예시 결과

| HOUR | COUNT |
| -----|-------|
| 9    | 1     |
| 10   | 2     |
| 11   | 13    |
| 12   | 10    |
| 13   | 14    |
| 14   | 9     |
| 15   | 7     |
| 16   | 10    |
| 17   | 12    |
| 18   | 16    |
| 19   | 2     |

---

# 참고

본 문제는 Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes" 데이터셋을 기반으로 하며, ODbL(Open Database License)의 적용을 받습니다.
