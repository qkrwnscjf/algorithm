import sys

A = int(sys.stdin.readline())

# 수열 리스트
P = list(map(int, sys.stdin.readline().split()))

dp = [1] * A # 각 수열마다의 수열 수 (위치가 곧 인덱스)

for i in range(1,A):
    for j in range(i):
        if P[i] < P[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))

             

