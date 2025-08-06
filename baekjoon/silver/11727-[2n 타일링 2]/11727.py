import sys

dp = [0] * 1001 #각 n이 1, 2, ... 일때의 결과값을 저장하는 dp


dp[1] = 1
dp[2] = 3


for i in range(3, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 2]) % 10007


print(dp[int(sys.stdin.readline())])
