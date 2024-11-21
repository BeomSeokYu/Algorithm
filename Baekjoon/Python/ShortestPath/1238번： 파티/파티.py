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
-> 다익스트라를 이용해야 함
'''

import sys, heapq
input = sys.stdin.readline

INF = int(1e9) #무한을 의미하는 상수

def dijkstra(graph, start, distance):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = distance[now] + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

N, M, X = map(int, input().split())

g = [[] for _ in range(N + 1)]
distance = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
  s, e, t = map(int, input().split())
  g[s].append((e, t))

dijkstra(g, X, distance[X])
for i in range(1, N + 1):
  dijkstra(g, i, distance[i])

cost = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
  cost[i] = distance[X][i] + distance[i][X]
  if (cost[i] > INF) :
    cost[i] = -1

print(max(cost))