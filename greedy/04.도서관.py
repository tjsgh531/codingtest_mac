import sys
input= sys.stdin.readline

N, M = map(int, input().split())

books = list(map(int, input().split()))
minus_books = []
plus_books = []

for i in books:
    if i < 0:
        minus_books.append(i)
    elif i > 0:
        plus_books.append(i)

minus_books.sort(reverse=True)
plus_books.sort()

ans = 0

while 1:
    ans -= minus_books[-1] * 2
    for _ in range(M):
        minus_books.pop()
