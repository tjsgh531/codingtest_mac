T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    n = scores[0]
    mean = (sum(scores)-n) / n
        