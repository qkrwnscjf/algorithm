# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램 작성
# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다.

N, K = map(int, input().split())

dp = [[1 for i in range(N+1)] for j in range(K+1)]

for i in range(2,K+1):
    for j in range(1,N+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N])



