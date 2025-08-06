import sys
import heapq

input = sys.stdin.readline
N = int(input())

problems = [tuple(map(int, input().split())) for _ in range(N)]
problems.sort()  # 마감일 기준 정렬

heap = []

for day, ramen in problems:
    heapq.heappush(heap, ramen)  # 힙에 라면 수만 저장
    
    if len(heap) > day:
        heapq.heappop(heap)  # 가장 작은 라면 수 제거

print(sum(heap))  # 남은 라면 수의 합이 최대 이익
