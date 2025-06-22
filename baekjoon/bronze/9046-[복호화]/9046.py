#복호화
results = []
for _ in range(int(input())):
    t = {}
    for w in input():
        if w == ' ':
            continue
        elif w not in t.keys():
            t[w] = 1
        else:
            t[w] += 1
    results.append(t)

for i in results:
    r = [k for k,v in i.items() if v==max(i.values())]
    if len(r) < 2:
        print(r[0])
    else:
        print('?')