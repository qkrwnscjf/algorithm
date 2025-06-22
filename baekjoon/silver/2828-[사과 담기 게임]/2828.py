"""""
# 사과 담기 게임
n, m = map(int, input().split()) #N은 전체크기, M은 바구니의 크기

# 사과의 개수 J가 주어진다
J = int(input())
#사과 J개가 떠러지는 위치 순서
for _ in range(J):
    location = int(input())
    # 몫을 이용하면 될거 같음.
    length = 0 #거리
    temp = m #현재 위치
    length += location // m
    temp = 
"""

n, m = map(int, input().split())
j = int(input())

start = 1
end = m
distance = 0

for _ in range(j):
    p = int(input())

    if p < start:
        distance += (start - p)
        start = p
        end = p + m - 1

    elif p > end:
        distance += (p - end)
        end = p
        start = end - m + 1

print(distance)