import sys
from collections import deque
input = sys.stdin.readline


def bfs(g, v, visited):
  visited[v] = True
  result_cnt = 1
  q = deque([(g[v], v)])
  tree = [ [] for _ in range(N + 1) ]
  while q:
    li = q.popleft()
    for u in li[0]:
      if not visited[u]:
        visited[u] = True
        result_cnt = result_cnt + 1
        q.append((g[u], u))
        tree[li[1]].append(u)
  return (tree, result_cnt)


N, R, Q = map(int, input().split())
g = [ [] for _ in range(N + 1) ]
visited = [ False for _ in range(N + 1) ]

for _ in range(N - 1):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

result = bfs(g, R, visited)
tree = result[0]

for _ in range(Q):
  visited = [ False for _ in range(N + 1) ]
  print(bfs(tree, int(input()), visited)[1])