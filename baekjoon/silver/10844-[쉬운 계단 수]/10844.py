# 45656 -> 인접한 모든 자리의 차이가 1 이를 계단 수라고 한다. 
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0은 계단 수 X

import sys

N = int(sys.stdin.readline())

dp = [0] * 101 #저장소 1 ~ 100 ()

# dp[1] = 9
# dp[2] = 17
# dp[3] = 

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % MOD)