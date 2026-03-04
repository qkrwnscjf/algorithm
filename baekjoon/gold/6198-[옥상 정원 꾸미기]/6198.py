import sys

# 다음 주석 코드는 시간초과 발생 (O(N^2)) -> 구현은 맞으나 시간이 초과 되니까..
'''''
N = int(sys.stdin.readline())

building = []
cnt = 0

for _ in range(N):
    building.append(int(sys.stdin.readline()))

for i in range(N-1):
    stack = []
    for j in range(i+1, N):
        if (building[i] > building[j]): # 보인다면
            cnt += 1
        else:
            break


print(cnt)
'''''

# 줄이려면? -> 스택사용 .

import sys

N = int(sys.stdin.readline())
buildings = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
stack = []  # 보이는 건물의 높이를 유지

for i in range(N):
    while stack and buildings[i] >= stack[-1]:
        # 현재 건물보다 작은 건물은 시야를 막을 수 없음 → pop
        stack.pop()
    cnt += len(stack)  # 현재 건물에서 보이는 오른쪽 건물 수
    stack.append(buildings[i])

print(cnt)
