import sys, heapq
input = sys.stdin.readline
INF = int(1e9)                              # 무한으로 사용할 수

v, e = map(int, input().split())            # 정점 수, 간선 수
k = int(input())                            # 시작 정점
g = [[] for _ in range(v + 1)]              # 해당 인덱스 : 정점 , 값 : 연결된 정점과 가중치
dist = [INF] * (v + 1)                      # 최단 거리 테이블

for i in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

def dijkstra(g, start, dist):
    q = []                                  # 우선순위 큐로 사용
    heapq.heappush(q, (0, start))           # 시작 노드로 가는 가중치 0으로 큐 삽입
    dist[start] = 0                         # 시작 노드 최단 거리 테이블 초기화
    while q:
        d, now = heapq.heappop(q)           # 최단 거리가 가장 짧은 노드 정보 꺼내옴
        if dist[now] < d:
            continue                        # 현재 노드가 이미 처리된 노드면 계속
        for i in g[now]:                    # 현재 노드의 인접 노드 루프
            cost = dist[now] + i[1]         # 비용(거리) 계산
            if cost < dist[i[0]]:           # 비용이 테이블보다 더 작으면
                dist[i[0]] = cost           # 테이블 갱신
                heapq.heappush(q, (cost, i[0])) # 우선순위 큐에 삽입

dijkstra(g, k, dist)                        # 다익스트라 알고리즘 수행

for i in range(1, v + 1):                   # 결과 출력
    print('INF') if dist[i] == INF else print(dist[i])