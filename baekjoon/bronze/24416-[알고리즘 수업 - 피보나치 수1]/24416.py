# 재귀 호출
def fib_1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_1(n-1) + fib_1(n-2) #시간초과 발생 : =1인 경우는 그냥 따로 설정하면 시간 최소화 가능!
    
def fib(n):
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]
        
# 다이나믹프로그래밍 
def fib_2(n):
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1): #3부터 : 실행횟수가 n-2
        f[i] = f[i-1] + f[i-2]
    return f[n]



n = int(input())

print(fib(n), n-2)