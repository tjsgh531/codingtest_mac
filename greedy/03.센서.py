"""
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))

gap = []
for i in range(len(sensor)-1):
    gap.append(sensor[i+1] - sensor[i])
        

gap.sort()
print(sum(gap[:N-K]))

--------------------------------------------------
"""

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))

gap = []
pre = sensor[0]
for i in sensor:
    gap.append(i - pre)
    pre = i

gap.sort()
for _ in range(K-1):
    gap.pop()
print(sum(gap))