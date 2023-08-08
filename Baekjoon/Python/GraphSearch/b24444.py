import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, s, visited, result):
    cnt = 1
    q = deque()
    q.append(s)
    result[s-1] = cnt
    visited[s] = True
    while q:
        u = q.popleft()
        g[u].sort()
        for v in g[u]:
            if not visited[v]:
                q.append(v)
                cnt += 1
                result[v-1] = cnt
                visited[v] = True
    return result

n, m, r = map(int,input().split())
g = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * n

for i in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in bfs(g, r, visited, result):
    print(i)