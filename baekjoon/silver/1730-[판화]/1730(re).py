N = int(input())  # 보드의 크기 입력
word = input()  # 명령어 입력 (예: DRDRRUU)

# 보드판 생성 (N x N 크기)
board = [['.'] * N for _ in range(N)]

# 시작 위치 (0, 0)에서 시작
x, y = 0, 0
board[x][y] = 'S'  # 시작 위치 표시 (S)

# 각 명령에 따른 이동
for direction in word:
    if direction == 'U' and x > 0:  # 위로 이동
        x -= 1
    elif direction == 'D' and x < N - 1:  # 아래로 이동
        x += 1
    elif direction == 'L' and y > 0:  # 왼쪽으로 이동
        y -= 1
    elif direction == 'R' and y < N - 1:  # 오른쪽으로 이동
        y += 1
    
    board[x][y] = '*'  # 이동한 위치를 '*'로 표시

# 보드판 출력
for row in board:
    print(' '.join(row))
