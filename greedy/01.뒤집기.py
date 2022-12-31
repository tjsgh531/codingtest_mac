import sys
input = sys.stdin.readline

S = input().strip()
cur = '?'
ans = 0

for i in S:
    if cur != i:
        ans+=1
        cur = i

print(ans//2)