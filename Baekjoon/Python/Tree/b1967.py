import sys
from collections import deque
input = sys.stdin.readline

def bfs(G, visited, s):
    visited[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for u, d in G[v]:
            if visited[u] < 0:
                visited[u] = visited[v] + d
                q.append(u)

N = int(input())
G = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

visited = [-1] * (N + 1)
bfs(G, visited, 1)
idx = visited.index(max(visited))
visited = [-1] * (N + 1)
bfs(G, visited, idx)
print(max(visited))