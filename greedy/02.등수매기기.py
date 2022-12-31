import sys
input = sys.stdin.readline

N = int(input())

predict = [ int(input()) for _ in range(N)]

cur = 1
ans = 0

for i in sorted(predict):
    ans += abs(i - cur)
    cur += 1

print(ans)