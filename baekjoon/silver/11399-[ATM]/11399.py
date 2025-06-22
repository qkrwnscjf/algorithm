n = int(input())
clock = 0

person = list(map(int, input().split()))

person.sort()


for i in range(1, n+1):
   clock += sum(person[:i])

print(clock)