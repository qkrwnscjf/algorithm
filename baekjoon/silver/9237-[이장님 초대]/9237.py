#이장님 초대
N = int(input())
#N만큼 입력 받고 싶으면, list사용
date = list(map(int, input().split()))

date.sort(reverse = True)

arr = []
for i in range(N):
    arr.append(date[i] + 1 + i) #여기서 i는 심는 날짜

result = max(arr) + 1 # +1은 이장님이 올 다음 날!

print(result)

