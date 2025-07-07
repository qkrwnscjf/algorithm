# 🐾 중성화 여부 파악하기

## 📋 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담고 있습니다. 각 동물의 **아이디**, **생물 종**, **보호 시작일**, **보호 시작 시 상태**, **이름**, **성별 및 중성화 여부** 등의 정보를 포함합니다.

보호소의 동물이 중성화되었는지 아닌지를 파악하려 합니다.  
`SEX_UPON_INTAKE` 컬럼에 `'Neutered'` 또는 `'Spayed'`라는 단어가 포함되어 있다면 **중성화된 동물**로 간주합니다.

## 🗃️ 테이블 구조

**ANIMAL_INS**

| 컬럼명            | 타입         | NULL 여부 | 설명                    |
|------------------|--------------|-----------|-------------------------|
| ANIMAL_ID        | VARCHAR(N)   | FALSE     | 동물의 ID              |
| ANIMAL_TYPE      | VARCHAR(N)   | FALSE     | 동물의 생물 종         |
| DATETIME         | DATETIME     | FALSE     | 보호 시작일            |
| INTAKE_CONDITION | VARCHAR(N)   | FALSE     | 보호 시작 시 상태      |
| NAME             | VARCHAR(N)   | TRUE      | 동물의 이름            |
| SEX_UPON_INTAKE  | VARCHAR(N)   | FALSE     | 성별 및 중성화 여부    |

## ✅ 출력 조건

- 동물의 `ANIMAL_ID`, `NAME`, 중성화 여부를 조회하세요.
- 중성화가 되어 있다면 `'O'`, 아니라면 `'X'`로 표시합니다.
- 결과는 `ANIMAL_ID` 기준으로 오름차순 정렬합니다.

## 💡 예시

### 입력 데이터 예시

| ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME       | SEX_UPON_INTAKE |
|-----------|--------------|---------------------|------------------|------------|-----------------|
| A355753   | Dog          | 2015-09-10 13:14:00 | Normal           | Elijah     | Neutered Male   |
| A373219   | Cat          | 2014-07-29 11:43:00 | Normal           | Ella       | Spayed Female   |
| A382192   | Dog          | 2015-03-13 13:14:00 | Normal           | Maxwell 2  | Intact Male     |

### 출력 예시

| ANIMAL_ID | NAME       | 중성화 |
|-----------|------------|--------|
| A355753   | Elijah     | O      |
| A373219   | Ella       | O      |
| A382192   | Maxwell 2  | X      |

## 🧠 풀이 참고

- SQL에서 `LIKE '%Neutered%'` 또는 `LIKE '%Spayed%'`를 활용하여 중성화 여부를 확인할 수 있습니다.
- `CASE WHEN` 구문으로 중성화 여부를 `'O'` 또는 `'X'`로 출력할 수 있습니다.

## 📎 출처

본 문제는 Kaggle의 **"Austin Animal Center Shelter Intakes and Outcomes"** 데이터셋을 기반으로 하며, [ODbL](https://opendatacommons.org/licenses/odbl/) 라이선스를 따릅니다.
