import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(V, visited, r):
    global order
    visited[r] = order
    V[r].sort(reverse=True)
    for i in V[r]:
        if visited[i] == 0:
            order += 1
            dfs(V, visited, i)

N, M, R = map(int, input().split())

order = 1
V = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    V[u].append(v)
    V[v].append(u)

dfs(V, visited, R)

for i in range(1, N + 1):
    print(visited[i])