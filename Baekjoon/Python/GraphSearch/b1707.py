import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

result = True
def dfs(G, visited, s, color):
    global result
    visited[s] = color
    color = 2 if color == 1 else 1
    for u in G[s]:
        if visited[u] == visited[s]:
            result = False
        if visited[u] == 0:
            visited[u] = color
            dfs(G, visited, u, color)

for _ in range(int(input())):
    result = True
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    for i in range(1, V + 1):
        if visited[i] == 0:
            dfs(G, visited, i, 1)
            if not result:
                break
    print('YES') if result else print('NO')