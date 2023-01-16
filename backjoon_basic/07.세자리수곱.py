# 제곱 : **
# 나머지 : //

A = int(input())
B = int(input())
ans = A*B
for i in range(3):
    temp = B % 10
    print(A * temp)
    B = B//10
print(ans)
    