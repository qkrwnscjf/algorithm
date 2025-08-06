import sys

N = int(sys.stdin.readline())

dp = [0] * (N+1) # 정답 저장 수
 
sq = [i ** 2 for i in range(N+1)] # 제곱 수 저장

print(dp)
print(sq)

for i in range(N+1):


#dp 문제는 규칙을 찾을 때까지 적어보는게 좋습니다.

number = int(input())

dp = [i for i in range(number + 1)]

for i in range(2, number + 1):
    for j in range(1, i + 1):
        square = j * j
        if square > i:
            break

        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1

print(dp[number])