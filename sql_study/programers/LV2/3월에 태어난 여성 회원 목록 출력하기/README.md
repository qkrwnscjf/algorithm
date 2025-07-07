# 👩‍💻 3월 생일 여성 회원 조회

## 📌 문제 설명

다음은 식당 리뷰 사이트의 회원 정보를 담은 `MEMBER_PROFILE` 테이블입니다.  
이 테이블에서 **생일이 3월**이고, **성별이 여성(`GENDER = 'W'`)**인 회원의 정보를 조회하는 SQL문을 작성하세요.  
단, **전화번호(`TLNO`)가 NULL**인 회원은 **제외**하고,  
**회원 ID(`MEMBER_ID`) 기준 오름차순 정렬**합니다.

---

## 🗂 테이블 구조

### MEMBER_PROFILE

| 컬럼명        | 타입           | NULL 허용 | 설명             |
|---------------|----------------|------------|------------------|
| MEMBER_ID     | VARCHAR(100)   | FALSE      | 회원 ID          |
| MEMBER_NAME   | VARCHAR(50)    | FALSE      | 회원 이름        |
| TLNO          | VARCHAR(50)    | TRUE       | 연락처           |
| GENDER        | VARCHAR(1)     | TRUE       | 성별 (`W`, `M`) |
| DATE_OF_BIRTH | DATE           | TRUE       | 생년월일         |

---

## ❓ 문제 요구사항

- 다음 조건을 만족하는 회원을 조회합니다:
  - `GENDER = 'W'`
  - 생일(`DATE_OF_BIRTH`)의 **월(Month)이 3월**
  - `TLNO IS NOT NULL`
- 출력 컬럼:
  - `MEMBER_ID`
  - `MEMBER_NAME`
  - `GENDER`
  - `DATE_OF_BIRTH`
- 정렬 기준:
  - `MEMBER_ID` **오름차순**

---

## 💡 예시

### MEMBER_PROFILE 테이블 예시

| MEMBER_ID            | MEMBER_NAME | TLNO         | GENDER | DATE_OF_BIRTH |
|----------------------|-------------|--------------|--------|----------------|
| jiho92@naver.com     | 이지호      | 01076432111  | W      | 1992-02-12     |
| jiyoon22@hotmail.com | 김지윤      | 01032324117  | W      | 1992-02-22     |
| jihoon93@hanmail.net | 김지훈      | 01023258688  | M      | 1993-02-23     |
| seoyeons@naver.com   | 박서연      | 01076482209  | W      | 1993-03-16     |
| yoonsy94@gmail.com   | 윤서연      | NULL         | W      | 1994-03-19     |

---

### ✅ 출력 예시

| MEMBER_ID          | MEMBER_NAME | GENDER | DATE_OF_BIRTH |
|--------------------|-------------|--------|----------------|
| seoyeons@naver.com | 박서연      | W      | 1993-03-16     |

- `윤서연`은 전화번호가 없으므로 제외
- `박서연`은 3월 생, 여성, 연락처 존재 → 조건 만족
