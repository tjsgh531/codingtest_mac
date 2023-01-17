temp = []
for _ in range(10):
    a = int(input()) % 42
    temp.append(a)

print(len(set(temp)))