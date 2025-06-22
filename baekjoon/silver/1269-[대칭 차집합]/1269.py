import sys
input = sys.stdin.readline

a, b=map(int, input().split())

a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

inter = a_list & b_list # 대칭 차집합 구하는 연산자 &

print(len(a_list)+len(b_list)- 2 * len(inter))