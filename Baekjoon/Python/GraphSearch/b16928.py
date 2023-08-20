# 뱀과 사다리 게임

import sys
from collections import deque

input = sys.stdin.readline

def bfs(G, visited):
    q = deque([1])
    while q:
        v = q.popleft()
        if G[v] == 0:
            for i in range(1, 7):
                if v + i > 100:
                    continue
                if visited[v + i] == 0 or visited[v + i] > visited[v] + 1:
                    visited[v + i] = visited[v] + 1
                    q.append(v + i)
        else:
            if visited[G[v]] == 0 or visited[G[v]] > visited[v]:
                visited[G[v]] = visited[v]
                q.append(G[v])

N, M = map(int, input().split())
G = [0] * 101
visited = [0] * 101

for _ in range(N + M):
    x, y = map(int, input().split())
    G[x] = y

bfs(G, visited)

print(visited[100])