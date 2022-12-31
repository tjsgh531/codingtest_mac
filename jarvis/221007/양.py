from collections import deque
from turtle import goto 

def bfs(row, col):
    q = deque()
    q.append((row, col))
    wolf_num = 0
    sheep_num = 0

    while q:
        item = q.popleft()
        y = item[0]
        x = item[1]
        if visited[y][x] == True:
            continue
        if graph[y][x] == 'o':
            sheep_num += 1
        elif graph[y][x] == 'v':
            wolf_num += 1

        visited[y][x] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= C or nx < 0 or ny < 0 or ny >= R:
                continue
            else:
                q.append((ny,nx))

    if wolf_num >= sheep_num:
        return (wolf_num, 0)
    else: 
        return (wolf_num, sheep_num)

R, C = map(int, (input().split()))
graph = [ input() for _ in range(R)]
visited = [[False]*C for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]    

wolf = 0
sheep = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            visited[i][j] = True

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            if graph[i][j] == 'v':
                temp = bfs(i, j)
                wolf += temp[0]
                sheep += temp[1]
            elif graph[i][j] == 'o':  
                temp = bfs(i, j)
                wolf += temp[0]
                sheep += temp[1]
print(sheep , wolf)