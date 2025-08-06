import sys, heapq

N = int(sys.stdin.readline())

#각 묶음의 카드의 수를 A, B라 하면 보통 
# 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다.

#예를 들어 10장, 20장, 40장의 묶음이 있다면 
# 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 
# (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 
# 그러나 10장과 40장을 합친 뒤, 
# 합친 50장 묶음과 20장을 합친다면
# (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

#N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 
# 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

page = []
ans = 0

for _ in range(N):
    card = int(sys.stdin.readline())
    
    heapq.heappush(page, card)

while len(page) > 1:
    a, b = heapq.heappop(page), heapq.heappop(page) 
    # 처음 :a : 10, b : 20 ,  ans = 30
    # page : [30, 40], ans = 30        
    # # a: 30 b : 40, ans = 30 + 70 
    ans += a + b
    heapq.heappush(page, a + b) # 왜 ans가 아닌 합만? : 누적값을 넣는게 아닌,
                                # 두 묶음의 합만 넣는것.
                            


print(ans)