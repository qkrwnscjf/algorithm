import sys

T = int(sys.stdin.readline())

#각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수

dp = [0] * 1000001
dp[1] = 1 # 1 
dp[2] = 2 # 2
dp[3] = 2 # 2 + 1, 1 + 2
dp[4] = 3 # 1 + 2 + 1, 1 + 3, 3 + 1
dp[5] = 5 # 1 + 4, 4 + 1, 1 + 3 + 1, 2 + 3, 3 + 2

# 전체 set 미리 생성
for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for _ in range(T):
    test = int(sys.stdin.readline())

    print(dp[test] % 1000000009)