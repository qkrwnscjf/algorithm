# 문제 설명

HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 활용하여 2022년도 한 해 평가 점수가 가장 높은 사원 정보를 조회하는 문제입니다.

- HR_GRADE 테이블에서 2022년 상반기, 하반기 점수를 합산하여 평가 점수를 계산합니다.
- 가장 높은 평가 점수를 받은 사원들의 점수, 사번, 성명, 직책, 이메일을 출력합니다.
- 출력 컬럼명은 각각 SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL 입니다.

---

## 테이블 구조

### HR_DEPARTMENT
| 컬럼명       | 타입      | Nullable |
|--------------|-----------|----------|
| DEPT_ID      | VARCHAR   | FALSE    |
| DEPT_NAME_KR | VARCHAR   | FALSE    |
| DEPT_NAME_EN | VARCHAR   | FALSE    |
| LOCATION     | VARCHAR   | FALSE    |

### HR_EMPLOYEES
| 컬럼명   | 타입      | Nullable |
|----------|-----------|----------|
| EMP_NO   | VARCHAR   | FALSE    |
| EMP_NAME | VARCHAR   | FALSE    |
| DEPT_ID  | VARCHAR   | FALSE    |
| POSITION | VARCHAR   | FALSE    |
| EMAIL    | VARCHAR   | FALSE    |
| COMP_TEL | VARCHAR   | FALSE    |
| HIRE_DATE| DATE      | FALSE    |
| SAL      | NUMBER    | FALSE    |

### HR_GRADE
| 컬럼명   | 타입    | Nullable |
|----------|---------|----------|
| EMP_NO   | VARCHAR | FALSE    |
| YEAR     | NUMBER  | FALSE    |
| HALF_YEAR| NUMBER  | FALSE    |
| SCORE    | NUMBER  | FALSE    |

---

## 요구사항

- 2022년도 상반기, 하반기 평가 점수를 합산하여 총 점수를 구합니다.
- 총 점수가 가장 높은 사원들의 정보를 출력합니다.
- 결과 컬럼명: SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL
- 동점자가 있을 경우 모두 출력합니다.
