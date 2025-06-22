#동전 1
n, k = map(int, input().split())  # 동전 종류 수 n, 목표 금액 k 입력
coin = [int(input()) for _ in range(n)]  # n개의 동전 가치 입력받아 리스트로 저장

dp = [0] * (k + 1)  # dp[i] = i원을 만드는 경우의 수
dp[0] = 1  # 0원을 만드는 방법은 '동전을 아무것도 사용하지 않는 1가지'뿐

# 각 동전에 대해 경우의 수를 누적
for c in coin:  # 동전 c를 기준으로
    for j in range(c, k + 1):  # c 이상부터 k까지 모든 금액 j에 대해
        dp[j] += dp[j - c]
        # dp[j - c]는 "j - c 원을 만드는 방법의 수"
        # 여기에 동전 c를 추가하면 j원을 만들 수 있음

print(dp[k])  # 최종적으로 k원을 만드는 경우의 수 출력




    