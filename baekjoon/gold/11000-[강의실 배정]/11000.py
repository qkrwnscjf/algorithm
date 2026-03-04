
import heapq

n = int(input())
arr = []
q = []
ans = 0
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr.sort(key = lambda x: (x[0], [1]))
heapq.heappush(q, arr[0][1])
ans += 1

for i in range(1, n):
  a, b = arr[i]
  if q[0] > a:
    heapq.heappush(q, b)
    ans += 1
  else:
    heapq.heappop(q)
    heapq.heappush(q, b)
print(ans)