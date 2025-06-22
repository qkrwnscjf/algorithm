N, M = map(int, input().split()) #첫 번째 줄에 이름의 길이를 받는다.

name_A, name_B = map(str, input().split())

alphabet = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
    'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
    'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
    'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
    'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2,
    'Z': 1
}

check_list = []

end = min(N, M) # 8

for i in range(end):
    check_list.append(name_A[i])
    check_list.append(name_B[i])

check_list.extend(name_A[end:]) # extend 사용법 알기
check_list.extend(name_B[end:])

check_list = [alphabet[ch] for ch in check_list]

#for i in range(len(check_list)):
 #   check_list[i] = alphabet[check_list[i]]

while len(check_list) != 2:
    temp_list = []
    temp_num = 0

    for i in range(len(check_list) - 1):
        temp_num = check_list[i] + check_list[i+1]
        if temp_num >= 10:
            temp_num -= 10
        temp_list.append(temp_num)
    check_list = temp_list


result = int(str(check_list[0]) + str(check_list[1]))
print(str(result) + "%")

