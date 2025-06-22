n = int(input())
arr = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

# 끝나는 시간 기준 정렬, 같으면 시작 시간 기준 정렬
arr.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start, end in arr:
    if start >= end_time:
        end_time = end
        count += 1

print(count)

#현재 arr = [[1,4], [x,y]....]로 저장해둔 상태.
#이때 마지막 for문에서 변수를 2개를 하면? -> 자동으로 [1,4]중에 앞에가 1 뒤에가 4로 연결 된다.