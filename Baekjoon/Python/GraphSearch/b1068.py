import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, visited, s):
    leaf_node = 0
    q = deque()
    if s == -1:
        return leaf_node
    if not visited[s]:
        visited[s] = True
        q.append(s)
    while q:
        v = q.popleft()
        if len(g[v]) == 0:
            leaf_node += 1
            continue
        for u in g[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    return leaf_node

N = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())
g = [[] for _ in range(N)]
visited = [False for _ in range(N)]
root = -1

for i in range(len(parent)):
    if parent[i] == remove_node or i == remove_node:
        continue
    if parent[i] == -1:
        root = i
        continue
    g[parent[i]].append(i)

print(bfs(g, visited, root))