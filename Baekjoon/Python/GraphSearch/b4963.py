import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(graph, x, y, w, h):
    graph[y][x] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    result = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                result += 1
                bfs(graph, x, y, w, h)

    print(result)