#약수의 합 2
#A = BC를 만족하는 C를 A의 약수, 약수의 합을 다 구하자 ?

""""
N = int(input())
 #1. f(N)을 먼저 구해보자.
f_arr = []
for i in range(1, N+1):
    if(N % i == 0):
        f_arr.append(i)

# 2. G(N) 구하기
g_arr = []
N -= 1
while(N > 0):
    for i in range(1, N+1):
        if(N % i == 0):
            g_arr.append(i)
        
    N -= 1

cnt_f = 0
cnt_g = 0
for i in range(len(f_arr)):
    cnt_f += f_arr[i]

for g in range(len(g_arr)):
    cnt_g += g_arr[g]

print(cnt_f + cnt_g)


""" ##시간 복잡도 O(N)을 충족시켜야함. 위에 코드는 O(n^2)
N = int(input())
result = 0

for i in range(1, N+1):
    result += i * (N // i) #약수로 찾는 것이 아니라 약수로 쓰이는 횟수를 생각하자!

print(result)

# 각 약수가 어떤 수의 약수로 등장했는가?
"""""
예 N = 6,
1 -> 6번
2 -> 3번
3 -> 2번
4 -> 1번
...
"""""

