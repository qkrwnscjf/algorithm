# b-a가 가장 큰 것을 출력 한다는건 arr[0]을 쓰면 된다는 소리!
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 3  # a = 3부터 시작
    found = False
    while cnt <= n // 2:
        b = n - cnt
        if is_prime(cnt) and is_prime(b):
            print(f"{n} = {cnt} + {b}")
            found = True
            break
        cnt += 2  # 홀수만 확인

    if not found:
        print("Goldbach's conjecture is wrong.")

    

    
            
    

