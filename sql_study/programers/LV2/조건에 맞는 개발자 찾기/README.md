# 문제 설명

DEVELOPERS 테이블과 SKILLCODES 테이블을 활용하여 Python 또는 C# 스킬을 가진 개발자의 정보를 조회하는 문제입니다.

- SKILLCODES 테이블의 CODE 컬럼은 2진수 비트로 각 스킬을 표현합니다.
- DEVELOPERS 테이블의 SKILL_CODE 컬럼은 여러 스킬의 비트 합으로 구성되어 있습니다.
- Python과 C# 스킬에 해당하는 CODE 값은 각각 256 (Python), 1024 (C#) 입니다.
- 이 두 스킬 중 하나라도 보유한 개발자(ID, EMAIL, FIRST_NAME, LAST_NAME)를 출력합니다.
- 결과는 ID를 기준으로 오름차순 정렬합니다.

---

## 테이블 구조

### SKILLCODES
| 컬럼명   | 타입     | Nullable | 설명              |
|----------|----------|----------|-------------------|
| NAME     | VARCHAR  | NO       | 스킬 이름         |
| CATEGORY | VARCHAR  | NO       | 스킬 범주         |
| CODE     | INTEGER  | NO       | 2진수 비트 코드   |

### DEVELOPERS
| 컬럼명      | 타입     | Nullable | 설명               |
|-------------|----------|----------|--------------------|
| ID          | VARCHAR  | NO       | 개발자 ID          |
| FIRST_NAME  | VARCHAR  | YES      | 이름               |
| LAST_NAME   | VARCHAR  | YES      | 성                 |
| EMAIL       | VARCHAR  | NO       | 이메일             |
| SKILL_CODE  | INTEGER  | NO       | 보유 스킬 비트 합  |

---

## 요구사항

- Python (CODE = 256) 또는 C# (CODE = 1024) 스킬 보유 여부를 bit 연산으로 확인
- 조건에 맞는 개발자 정보(ID, EMAIL, FIRST_NAME, LAST_NAME) 출력
- ID 기준 오름차순 정렬

---

## 예시

SKILLCODES 테이블 예시:

| NAME       | CATEGORY   | CODE |
|------------|------------|------|
| Python     | Back End   | 256  |
| C#         | Back End   | 1024 |
| Vue        | Front End  | 8192 |
| ...        | ...        | ...  |

DEVELOPERS 테이블 예시:

| ID   | FIRST_NAME | LAST_NAME | EMAIL                    | SKILL_CODE |
|------|------------|-----------|--------------------------|------------|
| D165 | Jerami     | Edwards   | jerami_edwards@grepp.co  | 400        |
| D164 | Kelly      | Grant     | kelly_grant@grepp.co     | 1024       |
| D162 | Cade       | Cunningham| cade_cunningham@grepp.co | 8452       |

출력 결과 예시:

| ID   | EMAIL                     | FIRST_NAME | LAST_NAME  |
|------|---------------------------|------------|------------|
| D162 | cade_cunningham@grepp.co  | Cade       | Cunningham |
| D164 | kelly_grant@grepp.co      | Kelly      | Grant      |
| D165 | jerami_edwards@grepp.co   | Jerami     | Edwards    |
