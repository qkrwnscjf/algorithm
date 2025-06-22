N = int(input())

for _ in range(N):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr[2])