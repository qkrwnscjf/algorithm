# 경제 카테고리 도서 목록 조회

## 📄 문제 설명

다음은 서점에서 판매 중인 도서 정보와 저자 정보를 담고 있는 `BOOK` 및 `AUTHOR` 테이블입니다.

### 📚 BOOK 테이블

| Column name     | Type        | Nullable | Description              |
|------------------|-------------|----------|--------------------------|
| BOOK_ID          | INTEGER     | FALSE    | 도서 ID                  |
| CATEGORY         | VARCHAR(N)  | FALSE    | 카테고리 (예: 경제, 인문, 소설 등) |
| AUTHOR_ID        | INTEGER     | FALSE    | 저자 ID                  |
| PRICE            | INTEGER     | FALSE    | 판매가 (원)              |
| PUBLISHED_DATE   | DATE        | FALSE    | 출판일                   |

### 🖋 AUTHOR 테이블

| Column name   | Type        | Nullable | Description  |
|---------------|-------------|----------|--------------|
| AUTHOR_ID     | INTEGER     | FALSE    | 저자 ID      |
| AUTHOR_NAME   | VARCHAR(N)  | FALSE    | 저자명       |

## ✅ 문제

`BOOK` 테이블에서 **카테고리가 '경제'**인 도서들의 다음 정보를 조회하는 SQL문을 작성하세요:

- `BOOK_ID`: 도서 ID
- `AUTHOR_NAME`: 저자명
- `PUBLISHED_DATE`: 출판일

📌 **출판일을 기준으로 오름차순 정렬**하여 결과를 출력하세요.

## 💡 예시

### BOOK 테이블

| BOOK_ID | CATEGORY | AUTHOR_ID | PRICE | PUBLISHED_DATE |
|---------|----------|-----------|-------|----------------|
| 1       | 인문     | 1         | 10000 | 2020-01-01     |
| 2       | 경제     | 1         | 9000  | 2021-04-11     |
| 3       | 경제     | 2         | 11000 | 2021-02-05     |

### AUTHOR 테이블

| AUTHOR_ID | AUTHOR_NAME |
|-----------|-------------|
| 1         | 홍길동      |
| 2         | 김영호      |

### 결과

| BOOK_ID | AUTHOR_NAME | PUBLISHED_DATE |
|---------|-------------|----------------|
| 3       | 김영호      | 2021-02-05     |
| 2       | 홍길동      | 2021-04-11     |

> ⚠️ `PUBLISHED_DATE`의 출력 포맷은 반드시 `YYYY-MM-DD` 형태여야 합니다.
