# 📦 USED_GOODS_BOARD - 2022년 10월 5일 중고거래 게시물 조회

## 📘 개요

이 프로젝트는 중고거래 게시판 데이터를 담고 있는 `USED_GOODS_BOARD` 테이블을 이용하여, 2022년 10월 5일에 등록된 게시글 정보를 조회하는 SQL 쿼리를 작성하는 문제입니다. 거래 상태는 한국어로 변환하여 출력해야 하며, 결과는 게시글 ID 기준으로 내림차순 정렬됩니다.

---

## 🗃️ 테이블 구조

### USED_GOODS_BOARD

| Column Name   | Type         | Nullable | Description           |
|---------------|--------------|----------|-----------------------|
| BOARD_ID      | VARCHAR(5)   | NOT NULL | 게시글 ID             |
| WRITER_ID     | VARCHAR(50)  | NOT NULL | 작성자 ID             |
| TITLE         | VARCHAR(100) | NOT NULL | 게시글 제목           |
| CONTENTS      | VARCHAR(1000)| NOT NULL | 게시글 내용           |
| PRICE         | NUMBER       | NOT NULL | 가격                  |
| CREATED_DATE  | DATE         | NOT NULL | 게시글 등록일         |
| STATUS        | VARCHAR(10)  | NOT NULL | 거래 상태 (SALE, RESERVED, DONE) |
| VIEWS         | NUMBER       | NOT NULL | 조회수                |

---

## 🎯 문제

2022년 10월 5일에 등록된 게시글의 `BOARD_ID`, `WRITER_ID`, `TITLE`, `PRICE`, `STATUS`를 조회하세요.

- `STATUS`는 다음과 같이 한글로 출력해야 합니다:
  - `SALE` → `판매중`
  - `RESERVED` → `예약중`
  - `DONE` → `거래완료`

- 결과는 `BOARD_ID` 기준으로 **내림차순** 정렬해야 합니다.

---

## 📝 출력 예시

### 입력 테이블 예시

| BOARD_ID | WRITER_ID  | TITLE          | CONTENTS                          | PRICE | CREATED_DATE | STATUS  | VIEWS |
|----------|------------|----------------|-----------------------------------|--------|---------------|---------|--------|
| B0007    | s2s2123    | 커피글라인더   | 새상품처럼 깨끗합니다.           | 7000   | 2022-10-04    | DONE    | 210    |
| B0008    | hong02     | 자전거 판매합니다 | 출퇴근용으로 구매했다가 사용하지 않아서 내놔요 | 40000  | 2022-10-04    | SALE    | 301    |
| B0009    | yawoong67  | 선반 팝니다    | 6단 선반. 환불 반품 안됩니다.    | 12000  | 2022-10-05    | DONE    | 202    |
| B0010    | keel1990   | 철제선반5단     | 철제선반 5단 조립식 팜           | 10000  | 2022-10-05    | SALE    | 194    |

### 출력 결과 예시

| BOARD_ID | WRITER_ID | TITLE        | PRICE | STATUS   |
|----------|-----------|--------------|--------|-----------|
| B0010    | keel1990  | 철제선반5단   | 10000 | 판매중    |
| B0009    | yawoong67 | 선반 팝니다   | 12000 | 거래완료  |

---

## 💡 SQL 정답 예시

```sql
SELECT 
    BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    CASE STATUS
        WHEN 'SALE' THEN '판매중'
        WHEN 'RESERVED' THEN '예약중'
        WHEN 'DONE' THEN '거래완료'
    END AS STATUS
FROM 
    USED_GOODS_BOARD
WHERE 
    TO_CHAR(CREATED_DATE, 'YYYY-MM-DD') = '2022-10-05'
ORDER BY 
    BOARD_ID DESC;
