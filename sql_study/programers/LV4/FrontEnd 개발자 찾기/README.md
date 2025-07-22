# Front End 스킬 보유 개발자 조회

## 문제 설명

`SKILLCODES` 테이블은 프로그래밍 언어나 프레임워크 등의 스킬 정보를 담고 있으며, 각각의 스킬은 `CATEGORY`, `NAME`, `CODE`로 구분됩니다. 이때 `CODE`는 2의 제곱수로 구성되어 있으며, 개발자가 보유한 전체 스킬은 `SKILL_CODE`라는 정수로 표현됩니다. `DEVELOPERS` 테이블은 각 개발자의 스킬을 해당 코드로 기록합니다.

개발자가 어떤 스킬을 보유했는지 확인하려면 `SKILL_CODE`와 특정 스킬의 `CODE` 값을 비트 연산하여 판단할 수 있습니다.

예를 들어, 어떤 개발자의 `SKILL_CODE`가 400일 경우 이는 이진수로 `110010000`에 해당하며, 이는 256, 128, 16의 스킬 코드를 모두 포함하고 있음을 의미합니다.

## 테이블 구조

### SKILLCODES

| 컬럼명   | 타입       | 제약조건          |
|----------|------------|-------------------|
| NAME     | VARCHAR(N) | UNIQUE, NOT NULL  |
| CATEGORY | VARCHAR(N) | NOT NULL          |
| CODE     | INTEGER    | UNIQUE, NOT NULL  |

### DEVELOPERS

| 컬럼명     | 타입       | 제약조건          |
|------------|------------|-------------------|
| ID         | VARCHAR(N) | UNIQUE, NOT NULL  |
| FIRST_NAME | VARCHAR(N) | NULLABLE          |
| LAST_NAME  | VARCHAR(N) | NULLABLE          |
| EMAIL      | VARCHAR(N) | UNIQUE, NOT NULL  |
| SKILL_CODE | INTEGER    | NOT NULL          |

## 문제 조건

- `CATEGORY`가 `'Front End'`인 스킬을 하나 이상 보유한 개발자를 조회합니다.
- `SKILL_CODE`와 각 Front End `CODE` 간의 비트 AND 연산을 통해 스킬 보유 여부를 판별할 수 있습니다.
- 조건을 만족하는 개발자의 ID, EMAIL, FIRST_NAME, LAST_NAME을 출력합니다.

## 출력 컬럼

- `ID`
- `EMAIL`
- `FIRST_NAME`
- `LAST_NAME`

## 정렬 조건

- `ID`를 기준으로 오름차순 정렬합니다.

## 예시 결과

| ID    | EMAIL                         | FIRST_NAME | LAST_NAME |
|-------|-------------------------------|------------|-----------|
| D161  | carsen_garza@grepp.co         | Carsen     | Garza     |
| D162  | cade_cunningham@grepp.co      | Cade       | Cunningham|
| D165  | jerami_edwards@grepp.co       | Jerami     | Edwards   |
