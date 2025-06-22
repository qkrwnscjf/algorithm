# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램 작성

n, m = map(int, input().split())

#최대공약수 
a = min(n, m)
arr = []
for i in range(1, a+1):
    if (n % i == 0 and m % i == 0):
        arr.append(i)

k = max(arr)
print(k)

#최소공배수
x = int(n * m / k)

print(x)
