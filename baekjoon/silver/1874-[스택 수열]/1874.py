#스택 수열
n = int(input())
stack = [] # [4, 3, 6, 8, 7, 5, 2, 1]
answer = [] # + - 넣을 리스트
cnt = 1 #1부터 반복문 내에서 하나씩 push

for _ in range(n):
    s = int(input()) #수열 값

    while cnt <= s:
        stack.append(cnt)
        answer.append('+') #push
        cnt += 1

    #첫번쨰 원소값 만큼 다 넣었다면?
    if stack[-1] == s:
        stack.pop()
        answer.append('-')

    else:
        answer.clear()
        answer.append('NO') 
        break  #없으면 NO 출력하기


for i in answer:
    print(i)

    
