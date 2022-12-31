from collections import deque

R, C = map(int, input().split())
graph = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)] 
wolf = 0
sheep = 0

dx = [0, 0, 1, -1, 0]
dy = [1, -1, 0, 0, 0]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    wolf_num = 0
    sheep_num = 0

    while q:
        item = q.pop()
        y = item[0]
        x = item[1]

        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= C or nx < 0 or ny >= R or ny < 0:
                continue
            if visited[ny][nx] == True:
                continue

            visited[ny][nx] = True
            
            if graph[ny][nx] == 'v':
                wolf_num += 1
            elif graph[ny][nx] == 'o':
                sheep_num += 1
            q.append((ny, nx))

    if wolf_num >= sheep_num:
        return (0, wolf_num)
    else:
        return (sheep_num, 0)


for i in range(R):
    for j in range(C):
        if graph[i][j] == '#':
            visited[i][j] = True

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v' and visited[i][j] == False:
            temp = bfs(i, j)
            sheep += temp[0]
            wolf += temp[1]
        if graph[i][j] == 'o' and visited[i][j] == False:
            temp = bfs(i, j)
            sheep += temp[0]
            wolf += temp[1]
print(f"{sheep} {wolf}")