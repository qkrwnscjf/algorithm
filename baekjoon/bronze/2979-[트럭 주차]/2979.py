a, b, c = map(int, input().split())

parking = [0] * 101  #전체 시간 길이

for _ in range(3):
    start, end = map(int, input().split())
    for t in range(start, end): 
        parking[t] += 1  #시간동안 차 수 증가

sum_fee = 0
for count in parking:
    if count == 1: #차 1개면
        sum_fee += a
    elif count == 2: #2개
        sum_fee += b * 2
    elif count == 3: #3개
        sum_fee += c * 3

print(sum_fee)
