#괄호
test = int(input()) #테스트 수 제공

for _ in range(test):
    #괄호 구성이 올바른가 -> VPS (YES)
    #아니면 NO
    stack = [] #저장소 생성 
    vps = input()
    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print("NO")

            


        

    
