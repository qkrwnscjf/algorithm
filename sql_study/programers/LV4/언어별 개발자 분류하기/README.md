# 개발자 GRADE 분류 및 정보 조회

## 문제 설명

`SKILLCODES` 테이블은 개발자들이 사용하는 프로그래밍 언어 및 기술 스택의 정보를 담고 있습니다.  
`DEVELOPERS` 테이블은 개발자의 스킬 정보를 비트 단위로 저장한 `SKILL_CODE` 컬럼을 통해, 보유 기술을 나타냅니다.

---

## 테이블 구조

### SKILLCODES

| 컬럼명   | 타입      | 설명                        |
|----------|-----------|-----------------------------|
| NAME     | VARCHAR   | 스킬 이름                   |
| CATEGORY | VARCHAR   | 스킬 분류 (Front/Back End 등) |
| CODE     | INTEGER   | 2의 제곱수 형태의 스킬 코드 |

### DEVELOPERS

| 컬럼명     | 타입     | 설명                      |
|------------|----------|---------------------------|
| ID         | VARCHAR  | 개발자 ID                 |
| FIRST_NAME | VARCHAR  | 이름                      |
| LAST_NAME  | VARCHAR  | 성                        |
| EMAIL      | VARCHAR  | 이메일                    |
| SKILL_CODE | INTEGER  | 보유한 스킬들의 비트 코드 |

---

## 문제 조건

- **GRADE 기준**
  - `A` : Front End 스킬과 Python 스킬을 **모두** 보유한 개발자
  - `B` : C# 스킬을 보유한 개발자
  - `C` : 그 외의 **Front End 스킬만** 보유한 개발자

- `GRADE`가 있는 개발자의 `GRADE`, `ID`, `EMAIL`을 조회합니다.
- 결과는 `GRADE`, `ID` 기준 **오름차순** 정렬합니다.

---

## 출력 컬럼

| 컬럼명 | 설명           |
|--------|----------------|
| GRADE  | 개발자 등급    |
| ID     | 개발자 ID      |
| EMAIL  | 개발자 이메일  |

---

## 예시 데이터

### SKILLCODES

| NAME       | CATEGORY   | CODE  |
|------------|------------|-------|
| C++        | Back End   | 4     |
| JavaScript | Front End  | 16    |
| Java       | Back End   | 128   |
| Python     | Back End   | 256   |
| C#         | Back End   | 1024  |
| React      | Front End  | 2048  |
| Vue        | Front End  | 8192  |
| Node.js    | Back End   | 16384 |

### DEVELOPERS

| ID   | FIRST_NAME | LAST_NAME  | EMAIL                         | SKILL_CODE |
|------|------------|------------|--------------------------------|------------|
| D165 | Jerami     | Edwards    | jerami_edwards@grepp.co       | 400        |
| D161 | Carsen     | Garza      | carsen_garza@grepp.co         | 2048       |
| D164 | Kelly      | Grant      | kelly_grant@grepp.co          | 1024       |
| D163 | Luka       | Cory       | luka_cory@grepp.co            | 16384      |
| D162 | Cade       | Cunningham | cade_cunningham@grepp.co      | 8452       |

### 예시 출력 결과

| GRADE | ID   | EMAIL                        |
|-------|------|------------------------------|
| A     | D162 | cade_cunningham@grepp.co     |
| A     | D165 | jerami_edwards@grepp.co      |
| B     | D164 | kelly_grant@grepp.co         |
| C     | D161 | carsen_garza@grepp.co        |

---
