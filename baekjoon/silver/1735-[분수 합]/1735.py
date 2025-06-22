a_arr = []
b_arr = []
arr = []

for i in range(2):
    a, b = map(int, input().split())
    a_arr.append(a)
    b_arr.append(b)

# 분수 덧셈
numerator = a_arr[1] * b_arr[0] + a_arr[0] * b_arr[1]
denominator = b_arr[0] * b_arr[1]

# 최대공약수 구해서 기약분수 만들기
cnt = min(numerator, denominator)

while cnt > 1:
    if numerator % cnt == 0 and denominator % cnt == 0:
        numerator //= cnt
        denominator //= cnt
        break
    cnt -= 1

print(numerator, denominator)

'''''
a, b = map(int, input().split())
c, d = map(int, input().split())

e = a * d + b * c
f = b * d

def gcd(e, f):
    while f:
        mod = f
        f = e % f
        e = mod
    return e

print(e//gcd(e, f), f//gcd(e, f))
'''''


