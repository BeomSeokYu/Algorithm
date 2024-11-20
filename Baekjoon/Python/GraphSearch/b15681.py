'''
BFS로 한 루트로 부터 이어지는 트리를 구할 수 있음 -> 최초 1회
구해진 트리를 다시 BFS를 통해 정점을 카운트함 -> 시간 초과 -> 매번 BFS로 Q입력마다 계산해야 함

DP 테이블을 사용하여 해당 정점을 루트로 하는 서브트리의 정점 수를 계산하여 저장 -> 1회 계산으로 입력되는 Q에 대해 결과 도출 가능할 것으로 보임
'''



import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

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
  return tree

def count_sub_tree_nodes(tree, root, cnt):
  cnt[root] = 1
  for v in tree[root]:
    count_sub_tree_nodes(tree, v, cnt)
    cnt[root] += cnt[v]

N, R, Q = map(int, input().split())
g = [ [] for _ in range(N + 1) ]
visited = [ False for _ in range(N + 1) ]

for _ in range(N - 1):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

# BFS를 통해 트리를 구함
tree = bfs(g, R, visited)

# DP 사용 해당 정점 루트로 하는 서브트리 정점 수 계산
cnt = [ 0 for _ in range(N + 1) ] # DP Table
count_sub_tree_nodes(tree, R, cnt)

# 해당 쿼리에 루트 입력 받아 정점 수 출력
for _ in range(Q):
  print(cnt[int(input())])