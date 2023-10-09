import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, visited, parent, s):
    visited[s] = True
    q = deque([s])
    while q:
        v = q.popleft()
        for u in g[v]:
            if not visited[u]:
                parent[u] = v
                visited[u] = True
                q.append(u)

N = int(input())
g = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        bfs(g, visited, parent, 1)

for i in range(2, N + 1):
    print(parent[i])