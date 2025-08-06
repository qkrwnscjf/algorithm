import sys
import math

n = int(sys.stdin.readline())

ring = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    a, b = ring[0] // math.gcd(ring[0], ring[i]), ring[i] // math.gcd(ring[0], ring[i])
    print(str(a) +  '/' + str(b))