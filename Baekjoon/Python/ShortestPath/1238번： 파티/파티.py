#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1238                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1238                           #+#        #+#      #+#     #
#    Solved: 2024/11/20 14:24:03 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
N - 노드(학생) 수
M - 단방향 간선 수
X - 모이는 노드 번호

각 노드가 노드 X를 거쳐 돌아오는 최단 거리 중 그 거리가 가장 긴 거리 출력

플루이드 워셜 이용 모든 정점에 대한 최단거리 정의 -> 시간 초과 -> 1000 ** 3
'''

import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 상수

def floyd_warshall(graph, n):
	for k in range(1, n + 1):
		for a in range(1, n + 1):
			for b in range(1, n + 1):
				graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

N, M, X = map(int, input().split())

g = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
	g[a][a] = 0

for i in range(M):
  s, e, t = map(int, input().split())
  g[s][e] = t

floyd_warshall(g, N)

cost = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
  cost[i] = g[i][X] + g[X][i]

print(max(cost))