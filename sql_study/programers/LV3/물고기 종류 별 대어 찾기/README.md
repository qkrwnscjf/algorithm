# 🎣 물고기 종류별 가장 큰 물고기 정보 조회

## 📘 문제 설명

낚시 앱에서 사용하는 `FISH_INFO` 테이블은 **잡은 물고기들**의 정보를 담고 있으며, `FISH_NAME_INFO` 테이블은 각 물고기 **종류에 해당하는 이름**을 담고 있습니다.

---

## 🔍 테이블 구조

### 🐟 FISH_INFO

| 컬럼명     | 타입    | NULL 허용 | 설명                          |
|------------|---------|------------|-------------------------------|
| `ID`       | INTEGER | FALSE      | 물고기의 고유 ID              |
| `FISH_TYPE`| INTEGER | FALSE      | 물고기의 종류 (숫자)          |
| `LENGTH`   | FLOAT   | TRUE       | 물고기의 길이 (cm)            |
| `TIME`     | DATE    | FALSE      | 물고기를 잡은 날짜            |

> 📌 단, **10cm 이하**의 물고기들은 `LENGTH`가 **NULL**로 저장됩니다.  
> 단, **모든 LENGTH가 NULL인 FISH_TYPE은 존재하지 않습니다.**

---

### 🐠 FISH_NAME_INFO

| 컬럼명     | 타입    | NULL 허용 | 설명              |
|------------|---------|------------|-------------------|
| `FISH_TYPE`| INTEGER | FALSE      | 물고기의 종류     |
| `FISH_NAME`| VARCHAR | FALSE      | 물고기 이름       |

---

## ✅ 문제

물고기 종류(`FISH_TYPE`) 별로 가장 큰 물고기의 다음 정보를 출력하는 SQL문을 작성하세요:

- 물고기 ID → `ID`
- 물고기 이름 → `FISH_NAME`
- 물고기 길이 → `LENGTH`

### 조건

- 결과는 `ID` 기준 **오름차순 정렬**
- 물고기 종류별 **가장 큰 물고기는 1마리만 존재**
- **10cm 이하인 물고기가 가장 큰 경우는 없음** → 즉, `LENGTH IS NOT NULL`

---

## 🧮 예시

### FISH_INFO

| ID | FISH_TYPE | LENGTH | TIME       |
|----|-----------|--------|------------|
| 0  | 0         | 30     | 2021-12-04 |
| 1  | 0         | 50     | 2020-03-07 |
| 2  | 0         | 40     | 2020-03-07 |
| 3  | 1         | 20     | 2022-03-09 |
| 4  | 1         | NULL   | 2022-04-08 |
| 5  | 2         | 13     | 2021-04-28 |
| 6  | 0         | 60     | 2021-07-27 |
| 7  | 0         | 55     | 2021-01-18 |
| 8  | 2         | 73     | 2020-01-28 |
| 9  | 1         | 73     | 2021-04-08 |
| 10 | 2         | 22     | 2020-06-28 |
| 11 | 2         | 17     | 2022-12-23 |

### FISH_NAME_INFO

| FISH_TYPE | FISH_NAME |
|-----------|-----------|
| 0         | BASS      |
| 1         | SNAPPER   |
| 2         | ANCHOVY   |

---

### 결과 출력 예시

| ID | FISH_NAME | LENGTH |
|----|-----------|--------|
| 6  | BASS      | 60     |
| 8  | ANCHOVY   | 73     |
| 9  | SNAPPER   | 73     |

---

## 💡 SQL 작성 팁

- `FISH_TYPE` 별로 `MAX(LENGTH)`를 먼저 구하고,
- 이를 `FISH_INFO`와 조인해서 **해당 최대 길이를 가진 행(ID 포함)** 추출
- `FISH_NAME_INFO`와 조인해 물고기 이름 붙이기
- `ORDER BY ID ASC`

---

## 🧾 출력 컬럼

| 컬럼명     | 설명              |
|------------|-------------------|
| `ID`       | 가장 큰 물고기의 ID |
| `FISH_NAME`| 물고기 이름         |
| `LENGTH`   | 물고기 길이         |
