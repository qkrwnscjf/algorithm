# 문제 설명

낚시앱에서 사용하는 FISH_INFO 테이블은 잡은 물고기들의 정보를 담고 있습니다. FISH_INFO 테이블의 구조는 다음과 같으며 ID, FISH_TYPE, LENGTH, TIME은 각각 잡은 물고기의 ID, 물고기의 종류(숫자), 잡은 물고기의 길이(cm), 물고기를 잡은 날짜를 나타냅니다.

| Column name | Type    | Nullable |
|-------------|---------|----------|
| ID          | INTEGER | FALSE    |
| FISH_TYPE   | INTEGER | FALSE    |
| LENGTH      | FLOAT   | TRUE     |
| TIME        | DATE    | FALSE    |

단, 잡은 물고기의 길이가 10cm 이하일 경우에는 LENGTH 가 NULL 이며, LENGTH 에 NULL 만 있는 경우는 없습니다.

---

## 문제

잡은 물고기의 평균 길이를 출력하는 SQL문을 작성해주세요.

- 평균 길이를 나타내는 컬럼명은 `AVERAGE_LENGTH` 로 지정합니다.
- 평균 길이는 소수점 셋째 자리에서 반올림합니다.
- 10cm 이하의 물고기들은 길이 10cm로 간주하여 평균을 계산합니다.

---

## 예시

예를 들어 FISH_INFO 테이블이 다음과 같다면

| ID | FISH_TYPE | LENGTH | TIME       |
|----|-----------|--------|------------|
| 0  | 0         | 30     | 2021/12/04 |
| 1  | 0         | 50     | 2020/03/07 |
| 2  | 0         | 40     | 2020/03/07 |
| 3  | 1         | 20     | 2022/03/09 |
| 4  | 1         | NULL   | 2022/04/08 |
| 5  | 2         | NULL   | 2021/04/28 |

- 10cm 이하인 물고기 (LENGTH가 NULL인 경우 포함)는 10cm로 간주합니다.
- 총 길이 합: 30 + 50 + 40 + 20 + 10 + 10 = 160
- 총 물고기 수: 6
- 평균 길이 = 160 / 6 = 26.666... → 반올림하여 26.67

결과는 다음과 같습니다.

| AVERAGE_LENGTH |
|----------------|
| 26.67          |

---

## 정답 예시 SQL

```sql
SELECT ROUND(
         AVG(
           CASE 
             WHEN LENGTH IS NULL OR LENGTH <= 10 THEN 10
             ELSE LENGTH
           END
         ), 2) AS AVERAGE_LENGTH
FROM FISH_INFO;
