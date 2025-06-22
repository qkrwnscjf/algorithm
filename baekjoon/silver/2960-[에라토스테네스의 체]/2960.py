#에라토스테네스의 체
'''''
1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다 (소수)
3. 소수를 지우고, 아직 지우지 않은 소수의 배수를 크기 순서대로 지움
4. 아직 모든 수를 지우지 않았다면, 다시 2번
'''''
N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)
            


