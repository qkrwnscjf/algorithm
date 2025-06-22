#빗물
h, w = map(int, input().split()) #세로 h 가로 w

height = list(map(int, input().split()))

#블록이 쌓인 높이를 의미(h)맨 왼쪽부터 

rainy = 0
# i : 현재위치(가로기준)
for i in range(1, w-1): # 양끝은 물을 채울 수 없음.
    #왼쪽 높이 - 오른쪽 높이 = 물 채워짐.
    #만약 오른쪽이 더 높거나 같은경우, 더해지지 않음.
    #양 옆에 자신보다 작은 높이의 블록이라면 물을 채울 수 없음.
    # 특정 위치에 물이 고이기 위해 자신보다 더 높은 블록으로 왼쪽 오른쪽이 둘러싼다.

    left = max(height[:i])
    right = max(height[i+1:])

    k = min(left, right) #더 낮은 쪽

    if height[i] < k:
        rainy += k - height[i]     

print(rainy)