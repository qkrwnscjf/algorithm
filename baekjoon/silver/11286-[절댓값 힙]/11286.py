# 절댓값 힙

# 1. 배열에 정수 x를 넣는다.(x != 0)
# 2. 배열에서 절댓값이 가장 작은 값 출력, 그 값을 배열에서 제거.
#    절댓값이 가장 작은 값이 여러개면 ? -> 가장 작은 수를 출력, 그 값을 배열에서 제거

import sys, heapq

abs_heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(abs_heap, (abs(num), num)) # abs : 절댓값
	else:
		if abs_heap:
			print(heapq.heappop(abs_heap)[1])
		else:
			print(0)


    