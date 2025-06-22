n = int(input())
room = [input() for _ in range(n)]

horizontal = 0
vertical = 0

# 가로 검사
for row in room:
    parts = row.split('X')
    for part in parts:
        if len(part) >= 2:
            horizontal += 1

# 세로 검사
for col in range(n):
    line = ''
    for row in range(n):
        line += room[row][col]
    parts = line.split('X')
    for part in parts:
        if len(part) >= 2:
            vertical += 1

print(horizontal, vertical)

    
