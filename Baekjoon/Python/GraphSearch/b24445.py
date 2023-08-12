import sys
from collections import deque

input = sys.stdin.readline

def bfs(V, r, visited):
    order = 1
    visited[r] = order
    q = deque([r])
    while q:
        u = q.popleft()
        V[u].sort(reverse=True)
        for v in V[u]:
            if visited[v] == 0:
                order += 1
                visited[v] = order
                q.append(v)

N, M, R = map(int, input().split())
V = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    V[u].append(v)
    V[v].append(u)

bfs(V, R, visited)

for i in range(1, N + 1):
    print(visited[i])