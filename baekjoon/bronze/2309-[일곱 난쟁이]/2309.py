#브루트푸스 알고리즘 기초 영역
arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)

# 두 명을 제외하는 방식으로 합이 100인 난쟁이를 찾기
for i in range(8):
    for j in range(i + 1, 9):
        selected = arr[:i] + arr[i+1:j] + arr[j+1:]
        if sum(selected) == 100:
            for height in sorted(selected):
                print(height)
            break
    else:
        continue
    break


