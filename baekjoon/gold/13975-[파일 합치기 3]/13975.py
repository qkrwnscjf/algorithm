# 파일 합치기
import sys, heapq

# 페이지를 각각의 파일로 만드는데, 두개씩 합쳐서 최종적으로 하나로.
# 이때, 두 개의 파일을 합칠 때 필요한 비용(시간) = 두 파일 크기의 합.
# 최소 비용으로 구하시오

T = int(sys.stdin.readline())

for _ in range(T):
	
    file = int(sys.stdin.readline())
    page = list(map(int, sys.stdin.readline().split()))
	
    heapq.heapify(page) # 배열을 힙큐로 변경
    
    ans = 0

    while len(page) > 1:
        temp = 0 # 중간 덧셈값 저장소
        a, b = heapq.heappop(page), heapq.heappop(page) 
        temp += a + b
        ans += temp
        heapq.heappush(page, temp)

    print(ans)

    


