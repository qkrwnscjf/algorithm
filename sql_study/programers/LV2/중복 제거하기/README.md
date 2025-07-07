# 🐶 보호소에 들어온 동물 이름 수 구하기

## 📌 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담고 있습니다.  
이 테이블에서 **중복되지 않는 유효한 동물 이름의 개수**를 구하세요.

- `NAME` 컬럼이 `NULL`인 경우는 제외합니다.
- 중복된 이름은 하나로 간주합니다.

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

- **유효한 이름의 수**를 출력합니다.
- 중복된 이름은 **하나로 처리**합니다.
- `NULL` 이름은 집계에서 제외합니다.

> 출력 컬럼명은 문제에서 제시된 `count`와 달라도 무관합니다.

---

## 💡 예시

### 입력 데이터 예시

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME      | SEX_UPON_INTAKE  |
|-----------|--------------|---------------------|------------------|-----------|------------------|
| A562649   | Dog          | 2014-03-20 18:06:00 | Sick             | NULL      | Spayed Female    |
| A412626   | Dog          | 2016-03-13 11:17:00 | Normal           | *Sam      | Neutered Male    |
| A563492   | Dog          | 2014-10-24 14:45:00 | Normal           | *Sam      | Neutered Male    |
| A513956   | Dog          | 2017-06-14 11:54:00 | Normal           | *Sweetie  | Spayed Female    |

### 출력 예시

| count |
|-------|
| 2     |

- 유효한 이름: `*Sam`, `*Sweetie`
- `NULL`은 제외되고, `*Sam`은 중복 제거됨

---

## 🧠 SQL 풀이 힌트
