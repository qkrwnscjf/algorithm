#스택
import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    # 어떻게 입력을 받을 것인가?
    command = sys.stdin.readline().split() #그냥 map이런거 쓰지 않고 split만 쓰면 자동으로 된다.
    
    if(command[0] == 'push'):
        command[1] = int(command[1])
        stack.append(command[1])
    
    elif(command[0] == 'pop'):
        if len(stack) == 0:
            print(-1)
        else:
            #print(stack[-1]) # LIFO구조
            #stack.remove(stack[-1])
            print(stack.pop())

    elif(command[0] == 'size'):
        print(len(stack))
    
    elif(command[0] == 'empty'):
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif(command[0] == 'top'):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) # LIFO구조
    