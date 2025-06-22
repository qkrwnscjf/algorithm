#2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

#각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
# 예: n = 3, 1, 11, 111(3으로 나뉘어짐), 1111, 11111, 111111(7로 나뉨)
while True:
    try:
        n = int(input())
    except:
        break  # 입력이 없으면 종료

    temp = 1
    count = 1

    while True:
        if temp % n == 0:
            print(count)
            break
        temp = temp * 10 + 1 # 1, 11, 111, 1111.....
        count += 1

        



    