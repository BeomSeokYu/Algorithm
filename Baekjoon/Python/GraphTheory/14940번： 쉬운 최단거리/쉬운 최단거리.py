#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14940                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14940                          #+#        #+#      #+#     #
#    Solved: 2024/12/04 10:14:52 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(g, dist, s, x_max, y_max):
  sx, sy, sd = s
  q = deque([])
  dist[sy][sx] = sd
  q.append(s)
  while q:
    x, y, d = q.popleft()
    for dx, dy in adj:
      nx, ny, nd = x + dx, y + dy, d + 1
      if nx < 0 or nx > x_max or ny < 0 or ny > y_max:
        continue
      if g[ny][nx] == 1 and (dist[ny][nx] == -1 or dist[ny][nx] > nd):
        dist[ny][nx] = nd
        q.append((nx, ny, nd))

n, m = map(int, input().split())
g = []
dist = [[] for _ in range(n)]
start = ()
for i in range(n):
  row = list(map(int, input().split()))
  try:
    start = (row.index(2), i, 0)
  except ValueError:
    pass
  g.append(row)
  for j in range(m):
    dist[i].append(0 if row[j] == 0 else -1)

bfs(g, dist, start, m-1, n-1)

for i in range(n):
  print(*dist[i])