import sys
from collections import deque

input = sys.stdin.readline

def bfs(visited, s):
    visited[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        inj = []
        if v - 1 >= 0:
            inj.append(v - 1)
        if v + 1 <= 100000:
            inj.append(v + 1)
        if v * 2 <= 100000:
            inj.append(v * 2)
        for u in inj:
            if visited[u] == -1 or visited[u] > visited[v] + 1:
                visited[u] = visited[v] + 1
                q.append(u)

N, K = map(int, input().split())

visited = [-1] * 100001

bfs(visited, N)

print(visited[K])