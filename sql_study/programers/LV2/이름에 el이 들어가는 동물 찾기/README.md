# 🐶 이름에 "el"이 들어간 개 찾기

## 📌 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물들의 정보를 담고 있습니다.  
한 사람이 돌아가신 할머니가 키우던 **이름에 'el'이 들어간 개**를 찾고 있습니다.  
이름에 `"el"`이 들어간 **강아지(Dog)**의 정보를 조회해주세요.

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

- **ANIMAL_TYPE이 'Dog'**인 데이터 중
- **이름(NAME)에 'el' 또는 'EL'이 포함된** 데이터를 조회
- **이름(NAME)을 기준으로 오름차순 정렬**
- 출력 컬럼: `ANIMAL_ID`, `NAME`

> 대소문자는 구분하지 않음 (즉, `el`, `El`, `EL`, `eL` 모두 허용)

---

## 💡 예시

### 입력 데이터 예시

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME        | SEX_UPON_INTAKE  |
|-----------|--------------|---------------------|------------------|-------------|------------------|
| A355753   | Dog          | 2015-09-10 13:14:00 | Normal           | Elijah      | Neutered Male    |
| A352872   | Dog          | 2015-07-09 17:51:00 | Aged             | Peanutbutter| Neutered Male    |
| A353259   | Dog          | 2016-05-08 12:57:00 | Injured          | Bj          | Neutered Male    |
| A373219   | Cat          | 2014-07-29 11:43:00 | Normal           | Ella        | Spayed Female    |
| A382192   | Dog          | 2015-03-13 13:14:00 | Normal           | Maxwell 2   | Intact Male      |

### 출력 예시

| ANIMAL_ID | NAME       |
|-----------|------------|
| A355753   | Elijah     |
| A382192   | Maxwell 2  |

---

