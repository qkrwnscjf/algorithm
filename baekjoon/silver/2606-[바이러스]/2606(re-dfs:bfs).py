#바이러스 : DFS/BFS 활용

#첫번째 줄에는 컴퓨터의 수가 주어진다.
computer = int(input())
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
connect = int(input())
virus = set()
virus.add(1)
while(connect > 0):
    a, b = map(int, input().split())
    if a in virus and b not in virus:
        virus.add(b)
    elif b in virus and a not in virus:
        virus.add(a)
        cnt += 1
    
    connect -= 1



print(len(virus) - 1)


computer = int(input())
connect = int(input())

# 연결 정보를 모두 저장
edges = []
for _ in range(connect):
    a, b = map(int, input().split())
    edges.append((a, b))

# 초기 감염 상태: 1번 컴퓨터
virus = set([1])
changed = True

# 감염 상태가 변화가 없을 때까지 반복
while changed:
    changed = False
    for a, b in edges:
        if a in virus and b not in virus:
            virus.add(b)
            changed = True
        elif b in virus and a not in virus:
            virus.add(a)
            changed = True

# 1번 컴퓨터 제외한 감염된 컴퓨터 수 출력
print(len(virus) - 1)
