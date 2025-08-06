import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))


cnt = 0

for i in range(1, N-1):
    if (arr[i] < arr[i-1]) and (arr[i] < arr[i+1]):
        cnt +=1 


print(cnt)
    