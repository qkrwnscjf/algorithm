test = int(input())

for _ in range(test):
    n = int(input())
    arr = []

    for i in range(n):
        num = input() #startswuith 사용을 위해 문자열로 보자.
        arr.append(num)
    
    arr.sort()
    
    word = 'YES'
    for i in range(1, len(arr)):
        if arr[i].startswith(arr[i-1]):
            word = 'NO'
            break
           
    
    print(word)



