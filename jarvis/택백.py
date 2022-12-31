
def dijktra(arr, start):
    target = arr[start]
    
    minval = min(target)
    idx = target.index(minval)


n, m = map(int , input().split())

graph = [[1001 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    row, col, data = map(int ,input().split())
    graph[row-1][col-1] = data

for i in range(n):
    visited = [False * n]
    // dijktra(i)
print(visited)
