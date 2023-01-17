temp = [0]*30
for _ in range(28):
    n = int(input()) -1
    temp[n] = 1

ans = 0
for i in range(30):
    if temp[i] == 0:
        print(i+1)
        ans += 1
        if ans == 2:
            break