#수 찾기

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in range(m):
    if (check[i] in arr):
        print(1)
    else:
        print(0)