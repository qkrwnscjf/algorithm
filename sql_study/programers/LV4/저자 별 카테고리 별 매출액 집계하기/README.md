# 문제 설명

서점에서 판매 중인 도서 정보(BOOK), 저자 정보(AUTHOR), 도서 판매량 정보(BOOK_SALES) 테이블이 있습니다.

---

## 테이블 구조

### BOOK

| 컬럼명        | 타입         | Nullable | 설명             |
|---------------|--------------|----------|------------------|
| BOOK_ID       | INTEGER      | FALSE    | 도서 ID          |
| CATEGORY      | VARCHAR(N)   | FALSE    | 카테고리 (경제, 인문, 소설, 생활, 기술) |
| AUTHOR_ID     | INTEGER      | FALSE    | 저자 ID          |
| PRICE         | INTEGER      | FALSE    | 판매가 (원)      |
| PUBLISHED_DATE| DATE         | FALSE    | 출판일           |

---

### AUTHOR

| 컬럼명       | 타입        | Nullable | 설명         |
|--------------|-------------|----------|--------------|
| AUTHOR_ID    | INTEGER     | FALSE    | 저자 ID      |
| AUTHOR_NAME  | VARCHAR(N)  | FALSE    | 저자명       |

---

### BOOK_SALES

| 컬럼명     | 타입       | Nullable | 설명         |
|------------|------------|----------|--------------|
| BOOK_ID    | INTEGER    | FALSE    | 도서 ID      |
| SALES_DATE | DATE       | FALSE    | 판매일       |
| SALES      | INTEGER    | FALSE    | 판매량       |

---

# 문제

- 2022년 1월 판매 데이터를 기준으로  
- 저자별, 카테고리별 매출액 (총 매출액 = 판매량 × 판매가) 을 구하세요.  
- 결과 컬럼: 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(TOTAL_SALES)  
- 정렬: 저자 ID 오름차순, 동일 저자 ID 내에서는 카테고리 내림차순

---

# 예시 데이터

### BOOK

| BOOK_ID | CATEGORY | AUTHOR_ID | PRICE | PUBLISHED_DATE |
|---------|----------|-----------|-------|----------------|
| 1       | 인문     | 1         | 10000 | 2020-01-01     |
| 2       | 경제     | 1         | 9000  | 2021-02-05     |
| 3       | 경제     | 2         | 9000  | 2021-03-11     |

---

### AUTHOR

| AUTHOR_ID | AUTHOR_NAME |
|-----------|-------------|
| 1         | 홍길동      |
| 2         | 김영호      |

---

### BOOK_SALES

| BOOK_ID | SALES_DATE  | SALES |
|---------|-------------|-------|
| 1       | 2022-01-01  | 2     |
| 2       | 2022-01-02  | 3     |
| 1       | 2022-01-05  | 1     |
| 2       | 2022-01-20  | 5     |
| 2       | 2022-01-21  | 6     |
| 3       | 2022-01-22  | 2     |
| 2       | 2022-02-11  | 3     |

---

# 매출액 계산

- BOOK_ID 1: 3권 × 10,000원 = 30,000원  
- BOOK_ID 2: 14권 × 9,000원 = 126,000원  
- BOOK_ID 3: 2권 × 9,000원 = 18,000원  

---

# 결과 예시

| AUTHOR_ID | AUTHOR_NAME | CATEGORY | TOTAL_SALES |
|-----------|-------------|----------|-------------|
| 1         | 홍길동      | 인문     | 30000       |
| 1         | 홍길동      | 경제     | 126000      |
| 2         | 김영호      | 경제     | 18000       |
