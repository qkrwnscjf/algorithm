# 🐶 보호소 동물 입양 대기자 조회

## 📄 테이블 정보

### ANIMAL_INS

| Column Name       | Type       | Nullable | Description               |
|-------------------|------------|----------|---------------------------|
| ANIMAL_ID         | VARCHAR(N) | FALSE    | 동물 ID                   |
| ANIMAL_TYPE       | VARCHAR(N) | FALSE    | 동물 종류 (개, 고양이 등) |
| DATETIME          | DATETIME   | FALSE    | 보호 시작일               |
| INTAKE_CONDITION  | VARCHAR(N) | FALSE    | 보호 시작 시 상태         |
| NAME              | VARCHAR(N) | TRUE     | 동물 이름                 |
| SEX_UPON_INTAKE   | VARCHAR(N) | FALSE    | 성별 및 중성화 여부       |

### ANIMAL_OUTS

| Column Name        | Type       | Nullable | Description               |
|--------------------|------------|----------|---------------------------|
| ANIMAL_ID          | VARCHAR(N) | FALSE    | 동물 ID (ANIMAL_INS FK)  |
| ANIMAL_TYPE        | VARCHAR(N) | FALSE    | 동물 종류                 |
| DATETIME           | DATETIME   | FALSE    | 입양일                   |
| NAME               | VARCHAR(N) | TRUE     | 동물 이름                 |
| SEX_UPON_OUTCOME   | VARCHAR(N) | FALSE    | 성별 및 중성화 여부       |

## ❓ 문제

아직 입양을 가지 못한 동물들 중,  
**가장 오래 보호소에 머물러 있는 동물 3마리**의 **이름**과 **보호 시작일**을  
**보호 시작일 순으로 조회**하는 SQL문을 작성하세요.

- 입양을 가지 못한 동물은 `ANIMAL_INS`에는 있고, `ANIMAL_OUTS`에는 없는 동물입니다.

## ✅ 출력 예시

| NAME   | DATETIME            |
|--------|---------------------|
| Shelly | 2015-01-29 15:01:00 |
| Jackie | 2016-01-03 16:25:00 |
| Benji  | 2016-04-19 13:28:00 |
