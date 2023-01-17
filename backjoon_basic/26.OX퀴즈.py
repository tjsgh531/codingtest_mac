T = int(input())
for _ in range(T):
    temp = input()
    comb = 1
    score = 0
    for i in temp:
        if i == 'O':
            score += comb
            comb += 1
        else:
            comb = 1
    print(score)