#단어 뒤집기

#문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램 작성.

test = int(input())

for _ in range(test):
    sentence = list(map(str, input().split()))

    for i in range(len(sentence)):
        sentence[i] =   sentence[i][::-1] #단어 뒤집기
        print(sentence[i], end = " ")