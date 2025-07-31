#약 팔기
#약 봉지 여러 개에 각각 적절한 수의 알약을 담아 늘어놓은 뒤,
# 약을 K알 달라고 하면 총 k알의 약이 들어이쓴 어떤 연속한 구간에 약봉지를 한번에 집어준다.
# 봉지를 일렬로 최대 2000개까지 가능. 

#출력 : 약봉지에 들어있어야 하는 약의 수를 출력

import sys
N = int(sys.stdin.readline())
result = []
for i in range(1000): # 1000번의
    result.append(1) # 1
for j in range(1000): # 1000번의
    result.append(1000) # 1000
print(len(result))
print(*result)



