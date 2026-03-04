import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = []

def div(x, y, n):
    color = matrix[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):

            if color != matrix[i][j]:
                for a in range(3):
                    for b in range(3):
                        div(x+ (n//3)*a, y + (n//3)*b, n//3)
                return
    if color == 1:
        cnt.append(1)

    elif color == 0:
        cnt.append(0)

    else:
        cnt.append(-1)

div(0,0,n)
print(cnt.count(-1), cnt.count(0), cnt.count(1), sep = '\n')