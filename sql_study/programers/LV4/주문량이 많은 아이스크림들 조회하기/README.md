# 아이스크림 주문량 상위 3맛 조회

## 문제 설명

아이스크림 가게의 상반기 주문 정보를 담은 `FIRST_HALF` 테이블과 7월의 주문 정보를 담은 `JULY` 테이블이 있습니다.

- `FIRST_HALF` 테이블은 다음과 같은 정보를 담고 있습니다:
  - `SHIPMENT_ID`: 출하 번호
  - `FLAVOR`: 아이스크림 맛 (기본 키)
  - `TOTAL_ORDER`: 상반기 총 주문량

- `JULY` 테이블은 다음과 같은 정보를 담고 있습니다:
  - `SHIPMENT_ID`: 출하 번호 (기본 키)
  - `FLAVOR`: 아이스크림 맛 (외래 키)
  - `TOTAL_ORDER`: 7월 총 주문량

> 한 가지 아이스크림 맛이 여러 출하 번호로 나눠 출하될 수 있으므로, `JULY` 테이블에는 동일한 `FLAVOR`가 여러 번 등장할 수 있습니다.

## 목표

- 7월 주문량과 상반기 주문량을 합산한 값이 **가장 큰 순서대로 상위 3개**의 아이스크림 맛을 조회하는 SQL 문을 작성하세요.

## 예시 데이터

### FIRST_HALF

| SHIPMENT_ID | FLAVOR           | TOTAL_ORDER |
|-------------|------------------|-------------|
| 101         | chocolate        | 3200        |
| 102         | vanilla          | 2800        |
| 103         | mint_chocolate   | 1700        |
| 104         | caramel          | 2600        |
| 105         | white_chocolate  | 3100        |
| 106         | peach            | 2450        |
| 107         | watermelon       | 2150        |
| 108         | mango            | 2900        |
| 109         | strawberry       | 3100        |
| 110         | melon            | 3150        |
| 111         | orange           | 2900        |
| 112         | pineapple        | 2900        |

### JULY

| SHIPMENT_ID | FLAVOR           | TOTAL_ORDER |
|-------------|------------------|-------------|
| 101         | chocolate        | 520         |
| 102         | vanilla          | 560         |
| 103         | mint_chocolate   | 400         |
| 104         | caramel          | 460         |
| 105         | white_chocolate  | 350         |
| 106         | peach            | 500         |
| 107         | watermelon       | 780         |
| 108         | mango            | 790         |
| 109         | strawberry       | 520         |
| 110         | melon            | 400         |
| 111         | orange           | 250         |
| 112         | pineapple        | 200         |
| 208         | mango            | 110         |
| 209         | strawberry       | 220         |

### 계산 예시

- `strawberry`: 3100 + (520 + 220) = 3840
- `mango`: 2900 + (790 + 110) = 3800
- `chocolate`: 3200 + 520 = 3720

## 출력 결과 예시

| FLAVOR     |
|------------|
| strawberry |
| mango      |
| chocolate  |
