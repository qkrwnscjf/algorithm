#연결 요소의 개수

''''
방향 없는 그래프가 주어졌을 때, 
연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
'''''

#DFS활용
cnt = 0 #DFS시 횟수 저장
n, m = map(int, input().split()) # 정점 N, 간선 M

dot = []

for _ in range(m):
    u, v = map(int, input().split()) # 간선의 양 끝점 u, v
    dot.append((u,v))


#출력 : 첫째 줄에 연결 요소의 개수를 출력 




