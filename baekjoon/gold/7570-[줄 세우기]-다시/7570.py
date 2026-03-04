import sys

# 줄 서있는 어린이 중 한 명을 선택하여 제일 앞이나 제일 뒤로 보낸다.
# 빈자리의 뒤에 있는 아이들이 한 칸씩 앞으로.
# 예를 들어, 5명의 어린이들에게 1부터 5까지의 번호가 주어져 있고, 
# #다음과 같은 순서로 줄 서있다고 하자.

#5 2 4 1 3

#위 방법을 이용해서 다음과 같이 번호순서대로 줄을 세울 수 있다.

#1번 어린이를 제일 앞으로 보낸다. (5 2 4 1 3 → 1 5 2 4 3)
#4번 어린이를 제일 뒤로 보낸다. (1 5 2 4 3 → 1 5 2 3 4)
#5번 어린이를 제일 뒤로 보낸다. (1 5 2 3 4 → 1 2 3 4 5) -> 최소 3번, 최솟값 찾기

n = int(sys.stdin.readline())

kids = list(map(int, sys.stdin.readline().split()))

sol = kids.sort() 

while(kids != sol):

    import sys

n = int(sys.stdin.readline())
kids = list(map(int, sys.stdin.readline().split()))

# 각 번호의 현재 인덱스를 기록
pos = [0] * (n + 1)
for i, num in enumerate(kids):
    pos[num] = i

# 정렬된 상태에서 연속된 숫자가 현재에서도 연속인 최대 길이 찾기
max_seq = 1
cur_seq = 1

for num in range(2, n + 1):
    if pos[num] > pos[num - 1]:
        cur_seq += 1
        max_seq = max(max_seq, cur_seq)
    else:
        cur_seq = 1

# 최소 이동 횟수 = 전체 인원 - 최대 연속 구간 길이
print(n - max_seq)



