# 중고 거래 게시판 - 다중 게시글 작성자 정보 조회

## 문제 설명

중고 거래 플랫폼에는 두 개의 테이블이 있습니다:

- **USED_GOODS_BOARD**: 중고 거래 게시물의 정보를 담고 있는 테이블
- **USED_GOODS_USER**: 사용자 정보를 담고 있는 테이블

이 문제에서는 **3건 이상의 게시물을 등록한 사용자**의 정보를 조회해야 합니다.

---

## 테이블 정보

### 📘 USED_GOODS_BOARD

| 컬럼명        | 타입       | 널 허용 | 설명                 |
|---------------|------------|----------|----------------------|
| BOARD_ID      | VARCHAR(5) | FALSE    | 게시글 ID            |
| WRITER_ID     | VARCHAR(50)| FALSE    | 작성자 ID            |
| TITLE         | VARCHAR(100)| FALSE   | 게시글 제목          |
| CONTENTS      | VARCHAR(1000)| FALSE  | 게시글 내용          |
| PRICE         | NUMBER     | FALSE    | 가격 (원)            |
| CREATED_DATE  | DATE       | FALSE    | 게시글 작성일        |
| STATUS        | VARCHAR(10)| FALSE    | 거래 상태 (예: DONE) |
| VIEWS         | NUMBER     | FALSE    | 조회수               |

---

### 📗 USED_GOODS_USER

| 컬럼명          | 타입         | 널 허용 | 설명              |
|------------------|--------------|---------|-------------------|
| USER_ID          | VARCHAR(50)  | FALSE   | 사용자 ID         |
| NICKNAME         | VARCHAR(100) | FALSE   | 닉네임            |
| CITY             | VARCHAR(100) | FALSE   | 시                |
| STREET_ADDRESS1  | VARCHAR(100) | FALSE   | 도로명 주소       |
| STREET_ADDRESS2  | VARCHAR(100) | TRUE    | 상세 주소         |
| TLNO             | VARCHAR(20)  | FALSE   | 전화번호 (숫자형) |

---

## 출력 요구사항

**조건을 만족하는 사용자 정보**를 다음과 같이 조회합니다:

- **조건**: 게시글을 **3건 이상 등록한 사용자**
- **출력 컬럼**:
  - 사용자 ID (`USER_ID`)
  - 닉네임 (`NICKNAME`)
  - 전체 주소: `CITY`, `STREET_ADDRESS1`, `STREET_ADDRESS2`를 **공백으로 연결**
  - 전화번호: 11자리 숫자에서 `xxx-xxxx-xxxx` 형식으로 하이픈 삽입
- **정렬**: 사용자 ID 기준 **내림차순**

---

## 예시 결과

| USER_ID   | NICKNAME | 전체주소                            | 전화번호        |
|-----------|----------|--------------------------------------|-----------------|
| dhfkzmf09 | 찐찐     | 성남시 분당구 수내로 13 A동 1107호 | 010-5342-2914   |

---

## 주의사항

- `STREET_ADDRESS2`가 `NULL`일 수도 있으므로 주소 연결 시 `NULL` 처리를 주의해야 합니다.
- 전화번호는 하이픈 형식을 맞춰야 하며, 일부 DB에서는 `SUBSTR`, `CONCAT` 등의 문자열 함수를 활용할 수 있습니다.

---

## 참고

- SQL 함수 예시: `CONCAT`, `SUBSTR`, `LPAD`, `CASE WHEN ...`
- 문자열 포맷팅: `SUBSTR(TLNO, 1, 3) || '-' || SUBSTR(TLNO, 4, 4) || '-' || SUBSTR(TLNO, 8)` 등

