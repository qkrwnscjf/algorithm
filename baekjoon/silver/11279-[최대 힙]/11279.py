#최대 힙 -> 큐나 스택 함수보단 힙큐가 효율(시간)
#heapq는 최소값을 pop하는 용도로만 지원된다.
import sys, heapq

arr = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	num = -1 * num #음수로 저장 
	if num != 0:
		heapq.heappush(arr, num) 
	else: # 0을 입력할 시
		if arr:
			print(-heapq.heappop(arr)) 
		else:
			print(0)