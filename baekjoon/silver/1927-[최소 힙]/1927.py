#최소 힙 -> 큐나 스택 함수보단 힙큐가 효율(시간)
import sys, heapq

arr = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num > 0:
		heapq.heappush(arr, num) 
	else: # 0을 입력할 시
		if arr:
			print(heapq.heappop(arr))
		else:
			print(0)
