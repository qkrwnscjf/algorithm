# 🐶 보호소 중성화 수술 동물 정보 조회

## 📘 문제 설명

동물 보호소에서는 보호 중에 **중성화 수술**을 진행한 동물의 정보를 파악하려고 합니다.

- **ANIMAL_INS** 테이블은 보호소에 들어온 동물의 정보를 담고 있습니다.
- **ANIMAL_OUTS** 테이블은 보호소에서 나간(입양된) 동물의 정보를 담고 있습니다.

보호소에 들어올 당시에는 **중성화되지 않았지만(Intact)**, 보호소를 나갈 당시에는 **중성화된(Spayed 또는 Neutered)** 동물의 정보를 조회해야 합니다.

---

## 📂 테이블 구조

### ANIMAL_INS

| 컬럼명            | 타입       | NULL 여부 | 설명               |
|------------------|------------|-----------|--------------------|
| ANIMAL_ID        | VARCHAR(N) | NOT NULL  | 동물의 ID          |
| ANIMAL_TYPE      | VARCHAR(N) | NOT NULL  | 생물 종            |
| DATETIME         | DATETIME   | NOT NULL  | 보호 시작일        |
| INTAKE_CONDITION | VARCHAR(N) | NOT NULL  | 입소 상태          |
| NAME             | VARCHAR(N) | NULLABLE  | 이름               |
| SEX_UPON_INTAKE  | VARCHAR(N) | NOT NULL  | 성별 및 중성화 여부 |

### ANIMAL_OUTS

| 컬럼명             | 타입       | NULL 여부 | 설명               |
|-------------------|------------|-----------|--------------------|
| ANIMAL_ID         | VARCHAR(N) | NOT NULL  | 동물의 ID          |
| ANIMAL_TYPE       | VARCHAR(N) | NOT NULL  | 생물 종            |
| DATETIME          | DATETIME   | NOT NULL  | 입양일             |
| NAME              | VARCHAR(N) | NULLABLE  | 이름               |
| SEX_UPON_OUTCOME  | VARCHAR(N) | NOT NULL  | 성별 및 중성화 여부 |

---

## 🎯 조회 조건

- 보호소에 **들어올 당시**에는 `"Intact"`가 포함된 성별 (중성화되지 않음)
- 보호소를 **나갈 당시**에는 `"Spayed"` 또는 `"Neutered"`가 포함된 성별 (중성화 완료)
- **ANIMAL_ID 기준 오름차순 정렬**

---

## ✅ 출력 컬럼

| 컬럼명       | 설명     |
|--------------|----------|
| ANIMAL_ID    | 동물 ID  |
| ANIMAL_TYPE  | 생물 종  |
| NAME         | 이름     |

---

## 💡 예시 출력

| ANIMAL_ID | ANIMAL_TYPE | NAME       |
|-----------|-------------|------------|
| A382192   | Dog         | Maxwell 2  |
| A410330   | Dog         | Chewy      |

---

