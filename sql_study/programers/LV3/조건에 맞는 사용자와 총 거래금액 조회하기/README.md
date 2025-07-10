# 🛒 완료된 중고 거래 총금액 기준 사용자 조회

## 📄 테이블 설명

### USED_GOODS_BOARD (중고 거래 게시판)

| 컬럼명       | 타입         | NULL 허용 | 설명                       |
|--------------|--------------|------------|----------------------------|
| BOARD_ID     | VARCHAR(5)   | FALSE      | 게시글 ID                  |
| WRITER_ID    | VARCHAR(50)  | FALSE      | 작성자 ID                  |
| TITLE        | VARCHAR(100) | FALSE      | 게시글 제목                |
| CONTENTS     | VARCHAR(1000)| FALSE      | 게시글 내용                |
| PRICE        | NUMBER       | FALSE      | 가격                       |
| CREATED_DATE | DATE         | FALSE      | 작성일                     |
| STATUS       | VARCHAR(10)  | FALSE      | 거래 상태 (SALE, DONE 등) |
| VIEWS        | NUMBER       | FALSE      | 조회수                     |

---

### USED_GOODS_USER (회원 정보)

| 컬럼명           | 타입         | NULL 허용 | 설명            |
|------------------|--------------|------------|-----------------|
| USER_ID          | VARCHAR(50)  | FALSE      | 회원 ID         |
| NICKNAME         | VARCHAR(100) | FALSE      | 닉네임          |
| CITY             | VARCHAR(100) | FALSE      | 시              |
| STREET_ADDRESS1  | VARCHAR(100) | FALSE      | 도로명 주소     |
| STREET_ADDRESS2  | VARCHAR(100) | TRUE       | 상세 주소       |
| TLNO             | VARCHAR(20)  | FALSE      | 전화번호        |

---

## ❓ 문제 설명

다음 조건에 따라 사용자 정보를 조회하는 SQL문을 작성하세요:

- 중고 거래 상태(`STATUS`)가 `DONE`인 게시글만 포함
- 사용자별 완료된 거래의 **총금액(PRICE 합계)**이 **70만 원 이상**
- 출력 항목:
  - 회원 ID (`USER_ID`)
  - 닉네임 (`NICKNAME`)
  - 총거래금액 (`TOTAL_SALES`)
- 결과는 **총거래금액 오름차순**으로 정렬

---

## ✅ 예시

### USED_GOODS_BOARD 예시 데이터

| BOARD_ID | WRITER_ID | TITLE                     | PRICE   | CREATED_DATE | STATUS | VIEWS |
|----------|-----------|---------------------------|---------|---------------|--------|--------|
| B0001    | zkzkdh1   | 캠핑의자                  | 25000   | 2022-11-29    | SALE   | 34     |
| B0002    | miyeon89  | 벽걸이 에어컨              | 100000  | 2022-11-29    | SALE   | 55     |
| B0003    | dhfkzmf09 | 에어팟 맥스               | 450000  | 2022-11-26    | DONE   | 67     |
| B0004    | sangjune1 | 파파야나인 포르쉐 푸쉬카   | 30000   | 2022-11-30    | DONE   | 78     |
| B0005    | zkzkdh1   | 애플워치7                 | 700000  | 2022-11-30    | DONE   | 99     |

### USED_GOODS_USER 예시 데이터

| USER_ID   | NICKNAME | CITY   | STREET_ADDRESS1        | STREET_ADDRESS2 | TLNO          |
|-----------|----------|--------|-------------------------|------------------|---------------|
| cjfwls91  | 점심만금식 | 성남시 | 분당구 내정로 185       | 501호            | 01036344964   |
| zkzkdh1   | 후후후    | 성남시 | 분당구 내정로 35        | 가동 1202호      | 01032777543   |
| spdlqj12  | 크크큭    | 성남시 | 분당구 수내로 206       | 2019동 801호     | 01087234922   |
| xlqpfh2   | 잉여킹    | 성남시 | 분당구 수내로 1         | 001-004          | 01064534911   |
| dhfkzmf09 | 찐찐      | 성남시 | 분당구 수내로 13        | A동 1107호       | 01053422914   |

---

### 예시 출력 결과

| USER_ID  | NICKNAME | TOTAL_SALES |
|----------|----------|-------------|
| zkzkdh1  | 후후후    | 700000      |

- `zkzkdh1`은 DONE 상태의 게시글 `B0005`(700000원)를 등록했기 때문에 조건에 해당됨

---

## 📌 요약

- 조건: 완료된 거래(`STATUS = 'DONE'`)
- 그룹: 사용자 ID(`WRITER_ID`)
- 필터: 총거래금액 ≥ 700,000
- 정렬: 총거래금액 오름차순
