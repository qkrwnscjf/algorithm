n= int(input())
location = []
for i in range(n):
    [x, y] = map(int, input().split())
    location.append([x, y])
location.sort()
for i in location:
    print(i[0], i[1])

