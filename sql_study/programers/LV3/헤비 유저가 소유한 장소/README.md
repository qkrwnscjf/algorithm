# 📄 헤비 유저의 공간 정보 조회

## 🗂️ 테이블 구조

### PLACES

| Column Name | Type     | Description              |
|-------------|----------|--------------------------|
| ID          | INT      | 공간의 고유 ID (Primary Key) |
| NAME        | VARCHAR  | 공간의 이름              |
| HOST_ID     | INT      | 공간 소유자의 유저 ID     |

---

## ❓ 문제 설명

- **PLACES** 테이블에는 공간 임대 서비스에 등록된 공간의 정보가 저장되어 있습니다.
- 이 서비스에서는 **공간을 2개 이상 등록한 사용자**를 **"헤비 유저"** 라고 정의합니다.
- "헤비 유저"가 등록한 **모든 공간의 정보**를 **ID 오름차순으로 조회**하는 SQL문을 작성해야 합니다.

---

## 💡 예시

다음과 같은 PLACES 테이블이 주어졌을 때:

| ID        | NAME                                                   | HOST_ID   |
|-----------|--------------------------------------------------------|-----------|
| 4431977   | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly        | 760849    |
| 5194998   | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly        | 760849    |
| 16045624  | Urban Jungle in the Heart of Melbourne                 | 30900122  |
| 17810814  | Stylish Bayside Retreat with a Luscious Garden         | 760849    |
| 22740286  | FREE PARKING - The Velvet Lux in Melbourne CBD         | 30900122  |
| 22868779  | ★ Fresh Fitzroy Pad with City Views! ★                | 21058208  |

- **760849**번 유저는 공간을 **3개** 등록 → 헤비 유저
- **30900122**번 유저는 공간을 **2개** 등록 → 헤비 유저
- **21058208**번 유저는 공간을 **1개** 등록 → 일반 유저

### ✅ 출력 결과:

| ID        | NAME                                                   | HOST_ID   |
|-----------|--------------------------------------------------------|-----------|
| 4431977   | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly        | 760849    |
| 5194998   | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly        | 760849    |
| 16045624  | Urban Jungle in the Heart of Melbourne                 | 30900122  |
| 17810814  | Stylish Bayside Retreat with a Luscious Garden         | 760849    |
| 22740286  | FREE PARKING - The Velvet Lux in Melbourne CBD         | 30900122  |

---


