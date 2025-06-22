#수 정렬하기4 (정렬 알고리즘 연습)
# 조건 : '수는 중복되지 않는다' -> set() 사용 가능.
import sys
n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
    arr.add(int(sys.stdin.readline()))

arr = sorted(arr, reverse = True)

for i in arr:
    print(i)