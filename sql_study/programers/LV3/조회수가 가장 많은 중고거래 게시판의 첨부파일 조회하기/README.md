# 📄 중고거래 게시판 최다 조회 게시물 첨부파일 경로 조회

## 🗂️ 테이블 구조

### USED_GOODS_BOARD

| Column Name   | Type        | Nullable | Description           |
|---------------|-------------|----------|-----------------------|
| BOARD_ID      | VARCHAR(5)  | FALSE    | 게시글 ID             |
| WRITER_ID     | VARCHAR(50) | FALSE    | 작성자 ID             |
| TITLE         | VARCHAR(100)| FALSE    | 게시글 제목           |
| CONTENTS      | VARCHAR(1000)| FALSE   | 게시글 내용           |
| PRICE         | NUMBER      | FALSE    | 가격                  |
| CREATED_DATE  | DATE        | FALSE    | 작성일                |
| STATUS        | VARCHAR(10) | FALSE    | 거래 상태             |
| VIEWS         | NUMBER      | FALSE    | 조회수                |

### USED_GOODS_FILE

| Column Name   | Type         | Nullable | Description           |
|---------------|--------------|----------|-----------------------|
| FILE_ID       | VARCHAR(10)  | FALSE    | 파일 ID               |
| FILE_EXT      | VARCHAR(5)   | FALSE    | 파일 확장자           |
| FILE_NAME     | VARCHAR(256) | FALSE    | 파일 이름             |
| BOARD_ID      | VARCHAR(10)  | FALSE    | 게시글 ID             |

---

## ❓ 문제 설명

- **조회수가 가장 높은 게시글**에 첨부된 파일들의 경로를 조회합니다.
- 경로 형식:  
  `/home/grep/src/게시글ID/파일ID파일이름.확장자`
- 결과는 **FILE_ID 기준 내림차순**으로 정렬되어야 합니다.
- 단, **조회수가 가장 높은 게시글은 오직 1개**입니다.

---

## 💡 예시 출력

| FILE_PATH                                    |
|---------------------------------------------|
| /home/grep/src/B0001/IMG_000002photo2.jpg    |
| /home/grep/src/B0001/IMG_000001photo1.jpg    |

---



