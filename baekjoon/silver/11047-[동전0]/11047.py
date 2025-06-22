n, k = map(int, input().split())
coin = []
cnt = 0
for _ in range(n):
    money = int(input())
    coin.append(money)

coin.sort(reverse=True) #오름차순으로 받았더니 그리디 할때 작은거부터 계산
#그리디 알고리즘 문제 풀 때 내림차순을 세팅하는게 편할듯

for i in coin:
    cnt += k // i
    k %= i

print(cnt)
        