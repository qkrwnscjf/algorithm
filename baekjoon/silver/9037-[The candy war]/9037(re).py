#시간초과
"""""
T = int(input())

for _ in range(T):
    child = int(input()) #5
    child_list = list(map(int, input().split())) # 2, 4, 7, 8, 9
    for i in range(child):
            if(child_list[i] % 2 != 0):
                child_list[i] += 1 # 짝수로 우선 다 맞춰주기 # 2, 4, 8 , 8, 10
    cnt = 0 #처음보정은 카운트 하지 않음.
    while(len(set(child_list)) != 1): #리스트 내 모든 원소가 같을떄까지 반복(set함수 적극 활용!!)
        

        give = [c // 2 for c in child_list]

        new_candies = [0] * child
        for i in range(child):
            new_candies[i] = child_list[i] - give[i] + give[i - 1]

        child_list = new_candies
        cnt += 1

    print(cnt)
"""

T = int(input())

for _ in range(T):
    child = int(input())  # 아이 수
    child_list = list(map(int, input().split()))  # 사탕 개수

    # 먼저 홀수인 아이들에게 선생님이 사탕을 1개 더해 짝수로 만든다.
    for i in range(child):
        if child_list[i] % 2 != 0:
            child_list[i] += 1  # 짝수로 보정

    cnt = 0
    # 사탕의 개수가 모두 같을 때까지 반복
    while True:
        # 모든 값이 같으면 종료
        if all(x == child_list[0] for x in child_list): #all > set 시간
            break

        # 1. 사탕을 나누는 계산
        give = [c // 2 for c in child_list]

        # 2. 나누기 후 새롭게 계산된 사탕 수
        new_candies = [0] * child
        for i in range(child):
            new_candies[i] = child_list[i] - give[i] + give[i - 1]

        # 3. 홀수인 사탕에 대해 선생님이 1개 더해 짝수로 만듦
        for i in range(child):
            if new_candies[i] % 2 != 0:
                new_candies[i] += 1

        child_list = new_candies
        cnt += 1

    print(cnt)


            
            




