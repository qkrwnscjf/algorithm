# 카드 구매하기 - dp

import sys

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))  # 인덱스 1부터 쓰기 위해 0 추가

dp = [0] * (N + 1)

for i in range(1, N + 1):  # i = 구매하려는 카드 수
    for j in range(1, i + 1):  # j = 카드팩 개수
        dp[i] = max(dp[i], dp[i - j] + P[j])

print(dp[-1])

