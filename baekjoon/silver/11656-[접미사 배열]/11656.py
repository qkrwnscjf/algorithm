#접미사 배열 -> 입력받은 단어에 대해 접미사 들을 사전순으로 출력.
word_set = set()
word = input()
for i in range(len(word)):
    word_set.add(word[i:])
    
word_set = sorted(word_set)

for i in word_set:
    print(i)
