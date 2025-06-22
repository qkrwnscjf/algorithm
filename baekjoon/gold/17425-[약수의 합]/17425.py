# 더 빠른 알고리즘 찾기
N = int(input())

for i in range(N):
    test = int(input())

    result = 0

    for i in range(1, test+1): # 다 뒤지지 않고 하는 법은 없을까?
        result += i * (test // i) 

    print(result)