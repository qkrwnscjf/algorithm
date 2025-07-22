# 🍽️ 서울 소재 식당 리뷰 평균 점수 조회

## 📘 문제 설명

다음은 식당의 정보를 담은 `REST_INFO` 테이블과 식당의 리뷰 정보를 담은 `REST_REVIEW` 테이블입니다.

- `REST_INFO`: 식당의 일반 정보 (이름, 음식 종류, 즐겨찾기 수, 주소 등)
- `REST_REVIEW`: 해당 식당의 리뷰 정보 (회원 ID, 점수, 리뷰일 등)

---

## 📂 테이블 구조

### REST_INFO

| 컬럼명       | 타입        | 설명             |
|--------------|-------------|------------------|
| REST_ID      | VARCHAR(5)  | 식당 ID          |
| REST_NAME    | VARCHAR(50) | 식당 이름        |
| FOOD_TYPE    | VARCHAR(20) | 음식 종류        |
| VIEWS        | NUMBER      | 조회수           |
| FAVORITES    | NUMBER      | 즐겨찾기 수      |
| PARKING_LOT  | VARCHAR(1)  | 주차장 유무      |
| ADDRESS      | VARCHAR(100)| 주소             |
| TEL          | VARCHAR(100)| 전화번호         |

### REST_REVIEW

| 컬럼명        | 타입        | 설명            |
|---------------|-------------|-----------------|
| REVIEW_ID     | VARCHAR(10) | 리뷰 ID         |
| REST_ID       | VARCHAR(10) | 식당 ID         |
| MEMBER_ID     | VARCHAR(100)| 회원 ID         |
| REVIEW_SCORE  | NUMBER      | 리뷰 점수       |
| REVIEW_TEXT   | VARCHAR(1000)| 리뷰 텍스트    |
| REVIEW_DATE   | DATE        | 리뷰 작성일     |

---

## 🎯 문제 조건

- 서울특별시에 위치한 식당만 대상으로 함 (`ADDRESS` 컬럼에 `"서울"` 포함)
- 식당 ID, 이름, 음식 종류, 즐겨찾기 수, 주소, **리뷰 평균 점수**를 조회
- 리뷰 평균 점수는 **소수점 3번째 자리에서 반올림**
- 결과 정렬 조건:
  1. 평균 점수 기준 **내림차순**
  2. 동일 평균 점수일 경우 즐겨찾기 수 기준 **내림차순**

---

## ✅ 출력 컬럼

| 컬럼명      | 설명             |
|-------------|------------------|
| REST_ID     | 식당 ID          |
| REST_NAME   | 식당 이름        |
| FOOD_TYPE   | 음식 종류        |
| FAVORITES   | 즐겨찾기 수      |
| ADDRESS     | 주소             |
| SCORE       | 평균 리뷰 점수   |

---

## 💡 예시 결과

| REST_ID | REST_NAME | FOOD_TYPE | FAVORITES | ADDRESS                             | SCORE |
|---------|-----------|-----------|-----------|-------------------------------------|-------|
| 00035   | 삼촌식당   | 일식      | 80        | 서울특별시 강서구 가로공원로76가길 | 4.5   |

---
