import sys

N = int(sys.stdin.readline())

dp = [0] * 1001
dp[1] = 10 #1, 2, 3, 4, 5, 6, 7, 8, 9
dp[2] = 55 
dp[3] = 220

# 11057
n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)