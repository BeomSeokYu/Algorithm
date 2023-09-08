import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, s):
    visited[s] = True
    q = deque([s])
    while q:
        v = q.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, visited, i)
        result += 1

print(result)