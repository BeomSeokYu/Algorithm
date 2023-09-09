import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
type_list = [('R'), ('G'), ('B'), ('R', 'G')]

def bfs(graph, type, x, y, N):
    q = deque()
    if graph[y][x] in type:
        graph[y][x] = 'V'
        q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x - dx[i], y - dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] in type:
                graph[ny][nx] = 'V'
                q.append((nx, ny))

N = int(input())
graph1 = []
for i in range(N):
    temp = list(input().rstrip())
    graph1.append(temp)
graph2 = copy.deepcopy(graph1)

res1 = 0
for i in range(N):
    for j in range(N):
        for k in range(3):
            if graph1[i][j] in type_list[k]:
                res1 += 1
                bfs(graph1, type_list[k], j, i, N)

res2 = 0
for i in range(N):
    for j in range(N):
        for k in range(2, 4):
            if graph2[i][j] in type_list[k]:
                res2 += 1
                bfs(graph2, type_list[k], j, i, N)

print(res1, res2)