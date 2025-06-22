#좌표정렬하기2

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key = lambda k : (k[1], k[0])) #lambda를 통한 y값으로 좌표 정렬


for i in arr:
    print(i[0], i[1])