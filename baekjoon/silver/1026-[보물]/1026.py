n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)




S = sum(a[i] * b[i] for i in range(n))

print(S)