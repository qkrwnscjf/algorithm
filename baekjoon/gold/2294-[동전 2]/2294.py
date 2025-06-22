#동적 프로그래밍 활용
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10001] * (k + 1)  # 충분히 큰 값으로 초기화
dp[0] = 0  # 0원을 만들기 위해 필요한 동전 수는 0

for c in coins:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[k] if dp[k] != 10001 else -1)
