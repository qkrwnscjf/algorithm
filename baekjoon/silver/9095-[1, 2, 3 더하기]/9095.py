#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
def func(x):
  if x==1:
    return 1
  elif x==2:
    return 2
  elif x==3:
    return 4
  else:
    return func(x-1)+func(x-2)+func(x-3)
  
t = int(input())


for _ in range(t):
    n = int(input())
    print(func(n))    

#알고리즘 문제를 풀때, 반복문을 쓴다는건 뭔가 규칙성이 있다는 뜻
#규칙성을 잘 탐구해보자!
