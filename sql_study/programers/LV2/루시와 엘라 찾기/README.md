# 🐾 특정 이름의 동물 조회하기

## 📌 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담고 있습니다.  
보호소에 들어온 동물 중, 이름이 다음 목록에 포함된 동물들의 정보를 조회하려고 합니다.

### 조회할 이름 목록:
- Lucy
- Ella
- Pickle
- Rogan
- Sabrina
- Mitty

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

- 이름(`NAME`)이 `Lucy`, `Ella`, `Pickle`, `Rogan`, `Sabrina`, `Mitty` 중 하나인 동물
- 출력 컬럼: `ANIMAL_ID`, `NAME`, `SEX_UPON_INTAKE`
- **`ANIMAL_ID` 기준으로 오름차순 정렬**

---

## 💡 예시

### 입력 데이터 예시

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
|-----------|--------------|---------------------|------------------|----------|------------------|
| A373219   | Cat          | 2014-07-29 11:43:00 | Normal           | Ella     | Spayed Female    |
| A377750   | Dog          | 2017-10-25 17:17:00 | Normal           | Lucy     | Spayed Female    |
| A353259   | Dog          | 2016-05-08 12:57:00 | Injured          | Bj       | Neutered Male    |
| A354540   | Cat          | 2014-12-11 11:48:00 | Normal           | Tux      | Neutered Male    |
| A354597   | Cat          | 2014-05-02 12:16:00 | Normal           | Ariel    | Spayed Female    |

### 출력 예시

| ANIMAL_ID | NAME | SEX_UPON_INTAKE |
|-----------|------|------------------|
| A373219   | Ella | Spayed Female    |
| A377750   | Lucy | Spayed Female    |

---


