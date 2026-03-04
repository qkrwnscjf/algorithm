import sys


N = int(sys.stdin.readline()) # 첫째 줄에 레벨의 수 N

cnt = 0
score = []

for _ in range(N):
    score.append(int(sys.stdin.readline()))

#감소만 시키는 구조라 맨 뒤의 값을 기준으로 탐색하면 괜찮지 않을까?

temp = score[-1] # 맨 뒤의 값.

for i in range(N-2, -1, -1):
    if score[i] >= temp:  
        cnt += (score[i] - (temp - 1))  # 현재 점수를 temp-1로 줄여야 함
        temp = temp - 1                 # 갱신: 다음 기준은 temp-1
    else:
        temp = score[i]                 # 이미 temp보다 작으면 그냥 유지


print(cnt)
        