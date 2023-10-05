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

V = int(input())
G = [[] for _ in range(V + 1)]
for i in range(V):
    li = list(map(int, input().split()))
    v = li.pop(0)
    for j in range(0, len(li) - 1, 2):
        G[v].append((li[j], li[j + 1]))

visited = [-1] * (V + 1)
bfs(G, visited, 1)
idx = visited.index(max(visited))
visited = [-1] * (V + 1)
bfs(G, visited, idx)
print(max(visited))