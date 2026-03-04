import sys 

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]

day = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

profit = 0 

for i in range(N):
    profit = max(profit, dp[i])

    if i + day[i][0] > N:
        continue

    dp[i + day[i][0]] = max(profit + day[i][1], dp[i + day[i][0]])

print(max(dp)) # dp의 최댓값 -> 최대비용