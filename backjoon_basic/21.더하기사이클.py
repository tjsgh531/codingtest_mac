N = int(input())
newNum = N
ans = 0

while 1:
    a = newNum // 10
    b = newNum % 10
    newNum = b * 10 + ((a+b)%10)
    ans += 1

    if newNum == N:
        break

print(ans) 