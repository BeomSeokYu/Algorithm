import sys, copy
from collections import deque
input = sys.stdin.readline

def bfs(graph, visited, s, e):
    if not graph[s]:
        return
    visited[s] += 1
    if s == e:
        return
    q = deque([s])
    while q:
        v = q.popleft()
        for u, _d in graph[v]:
            if visited[u] < 0 or visited[u] > visited[v] + _d:
                visited[u] = visited[v] + _d
                q.append(u)

N, E = map(int, input().split())

graph = [[] for i in range(N + 1)]
visited_mid = [-1] * (N + 1)
visited_list = []
for i in range(4):
    visited_list.append(copy.deepcopy(visited_mid))
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
li = [(1, v1), (v2, N), (1, v2), (v1, N)]
dlist = []
for i in range(4):
    s, e = li[i]
    bfs(graph, visited_list[i], s, e)
    dlist.append(visited_list[i][e])
bfs(graph, visited_mid, v1, v2)

result1 = dlist[0] + dlist[1]
result2 = dlist[2] + dlist[3]
condition = dlist[0] == -1 or dlist[1] == -1 or dlist[2] == -1 or dlist[3] == -1
result = min(result1, result2) + visited_mid[v2]
print(result if result > 0 and not condition else -1)