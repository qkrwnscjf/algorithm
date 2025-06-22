#isdigit() -> 문자열에서 숫자 있는지 확인

n = int(input())
answer = []

for _ in range(n):
    result = ''
    word = input()
    for i in word:
        if i.isdigit() == True:
            result += i
        else:
            if result:
                answer.append(int(result)) #잘라서 배열에 저장해야함
                result = ''
    if result != '':
        answer.append(int(result))

answer.sort()
for i in answer:
    print(i)