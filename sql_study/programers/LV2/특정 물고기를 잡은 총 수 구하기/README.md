# 🎣 BASS와 SNAPPER 물고기 수 세기

## 📘 문제 설명

낚시 앱에서 사용하는 `FISH_INFO` 테이블은 사용자가 잡은 물고기에 대한 정보를 담고 있으며, `FISH_NAME_INFO` 테이블은 각 물고기 종류의 이름 정보를 담고 있습니다.

### FISH_INFO 테이블 구조

| Column name | Type   | Nullable | 설명                    |
|-------------|--------|----------|-------------------------|
| ID          | INTEGER| FALSE    | 잡은 물고기의 고유 ID   |
| FISH_TYPE   | INTEGER| FALSE    | 물고기 종류 (숫자형)     |
| LENGTH      | FLOAT  | TRUE     | 물고기의 길이 (cm)      |
| TIME        | DATE   | FALSE    | 물고기를 잡은 날짜      |

> **참고**: 잡은 물고기의 길이가 10cm 이하일 경우 `LENGTH` 는 `NULL` 이 됩니다.  
> 단, `LENGTH` 값이 전부 `NULL`인 경우는 없습니다.

---

### FISH_NAME_INFO 테이블 구조

| Column name | Type     | Nullable | 설명             |
|-------------|----------|----------|------------------|
| FISH_TYPE   | INTEGER  | FALSE    | 물고기 종류 코드 |
| FISH_NAME   | VARCHAR  | FALSE    | 물고기 이름      |

---

## 🧩 문제 목표

`FISH_INFO` 테이블에서 **잡은 물고기 중 'BASS'와 'SNAPPER'의 총 수**를 구하는 SQL 쿼리를 작성하세요.

- 출력 컬럼명은 `FISH_COUNT`로 지정해야 합니다.

---

## 🐟 예시 데이터

### 🎣 FISH_INFO

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
| 9  | 2         | 73     | 2021-04-08 |
| 10 | 2         | 22     | 2020-06-28 |
| 11 | 2         | 17     | 2022-12-23 |

### 🐠 FISH_NAME_INFO

| FISH_TYPE | FISH_NAME |
|-----------|-----------|
| 0         | BASS      |
| 1         | SNAPPER   |
| 2         | ANCHOVY   |

---

## ✅ 기대 결과

| FISH_COUNT |
|------------|
| 7          |

- **BASS** (`FISH_TYPE` 0): 총 5마리
- **SNAPPER** (`FISH_TYPE` 1): 총 2마리  
→ 총합: **7마리**

---


