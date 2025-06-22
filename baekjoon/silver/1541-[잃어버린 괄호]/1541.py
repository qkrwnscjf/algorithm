#예제를 보아하니 최소를 만드려면, '-'를 기준으로 나누면 된다.

math = input().split('-') # '-' 기준 분리

hap = []
for i in math: # '+' 기준 분리하여 합을 구함
    temp = list(map(int, i.split('+'))) 
    hap.append(sum(temp))

result = hap[0] 
for i in hap[1:]: # hap의 1번 이후 값들을 순차적으로 result에서 빼줌
    result -= i

print(result)
