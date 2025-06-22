#좌표 압축
n = int(input())
x = list(map(int, input().split())) #둘째 줄에는 공백 한 칸으로 구분된 좌표가 주어진다.

# 1. 중복 제거 + 정렬
x_zip = sorted(set(x))

# 2. 압축 인덱스 매핑 딕셔너리 생성
coord_dict = {num: idx for idx, num in enumerate(x_zip)} #enumerate로 idx 설정 가능

# 3. 원래 리스트에서 해당 인덱스 출력
compressed = [coord_dict[num] for num in x]

for i in range(n):
    print(compressed[i], end=" ")




