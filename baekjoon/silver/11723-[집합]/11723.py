'''''
n = int(input())
s = set() # list말고 set을 써야 시간 복잡도 아낌

for _ in range(n):
    inputs = input().split()

    if inputs[0] == 'add':
        s.add(int(inputs[1]))

    elif inputs[0] == 'remove':
        s.discard(int(inputs[1]))  # 존재하지 않아도 에러 X

    elif inputs[0] == 'check':
        print(1 if int(inputs[1]) in s else 0)

    elif inputs[0] == 'toggle':
        x = int(inputs[1])
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    elif inputs[0] == 'all':
        s = set(range(1, 21))

    elif inputs[0] == 'empty':
        s.clear()
    '''

import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
  arr = list(input().split())
  c = arr[0]
  if c == 'add':
    s.add(int(arr[1]))
  elif c == 'remove':
    try:
      s.remove(int(arr[1]))
    except:
      pass
  elif c == 'check':
    if int(arr[1]) in s:
        print(1)
    else:
      print(0)
  elif c == 'toggle':
    if int(arr[1]) in s:
      s.remove(int(arr[1]))
    else:
      s.add(int(arr[1]))
  elif c == 'all':
    s = set([i for i in range(1,21)])
  else:
    s = set()

