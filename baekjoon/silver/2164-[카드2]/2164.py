#자료구조 -> 카드2 
#list사용 -> 시간 초과 O(n^2)
'''''
import sys
n = int(sys.stdin.readline())
card = []

for i in range(1, n+1):
    card.append(i)

while(len(card) != 1):
    card.remove(card[0])
    temp = card[0]
    card.remove(card[0])
    card.append(temp)
    
print(card[0])
'''''
#deque사용 : 시간도 그렇고 가장 효율, 그렇지만 익숙치 않음 공부해야함.(O(1)!!)
from collections import deque #deque사용법은 자료구조 공부에 도움

n = int(input())
card = deque(range(1, n + 1))

while len(card) > 1:
    card.popleft()             # 제일 위 카드 제거
    card.append(card.popleft())  # 다음 카드를 맨 아래로 이동

print(card[0])


#set : set으로는 풀 수가 없다..


