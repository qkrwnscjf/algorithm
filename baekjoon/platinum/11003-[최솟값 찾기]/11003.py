# 12, 3
# D(i) = A(i-L+1) ~ A(i) 중 최소

# 1 5 2 3 6 2 3 7 3 5 2 6 , L = 3?
# D(i) = A(i - 2) ~ A (i) 중 최소 

import sys
from collections import deque
 
input = sys.stdin.readline
 
N, L = map(int, input().split())
A = list(map(int, input().split()))
 
dq = deque()
for i in range(N):
	
    while dq and (dq[-1][1] > A[i]): # 1
        dq.pop()
	
    dq.append((i + 1, A[i]))         # 2
	
    if dq[-1][0] - dq[0][0] >= L:    # 3
        dq.popleft()
 
    print(dq[0][1], end=' ')