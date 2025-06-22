#비밀번호 찾기(딕셔너리 활용)
import sys
n, m = map(int, sys.stdin.readline().split())
passwords = {}

for _ in range(n):
    site, code = sys.stdin.readline().split()
    passwords[site] = code

for _ in range(m):
    find = sys.stdin.readline().strip()
    print(passwords[find])

'''''
1.passwords는 딕셔너리 자료형(dict) 으로, 키(key)와 값(value)을 한 쌍으로 저장합니다.

2.site는 딕셔너리의 키(key) 역할을 하고, code는 값(value) 으로 저장됩니다.

3.passwords[site] = code는 해당 사이트 주소(site)에 대한 비밀번호(code)를 저장하거나 갱신합니다.

4. 만약 같은 site가 이미 존재하면, 기존 값을 새로운 code로 덮어쓰기합니다.

5. 이후 passwords[site]로 빠르게(시간복잡도 O(1)) 해당 비밀번호를 조회할 수 있습니다.

'''''

