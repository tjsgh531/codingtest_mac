N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
temp = []

for i in scores:
    temp.append(i/max_score *100)
print(sum(temp)/N)