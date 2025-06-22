n, m = map(int, input().split())
true = set()
false = set() #메모리 줄일거면 제발 set함수 적극 활용!

for i in range(n):
    true.add(input())

for i in range(m):
    false.add(input())

result = sorted(list(true & false))

print(len(result))

for i in result:
    print(i)





