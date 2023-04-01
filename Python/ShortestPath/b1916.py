import sys, heapq
input = sys.stdin.readline
INF = int(1e9)                                          # 무한 상수 설정

def dijkstra(g, s, table):
    q = []
    heapq.heappush(q, (0, s))                           # 우선순위 큐에 시작 노드 삽입
    table[s] = 0                                        # 최단거리 테이블 시작 노드 초기화

    while q:                                            # 큐가 빌 때까지 반복
        c, now = heapq.heappop(q)                       # 큐에서 비용 최솟값, 노드 가져옴
        if table[now] < c:                              # 테이블의 비용이 더 작으면 이미 계산된 것
            continue
        for node in g[now]:                             # 인접 리스트 순환
            cost = table[now] + node[1]                 # 인접 리스트들 비용 계산
            if cost < table[node[0]] :                  # 테이블보다 비용이 적으면
                table[node[0]] = cost                   # 테이블 갱신
                heapq.heappush(q, (cost, node[0]))      # 큐에 삽입


n = int(input())                                        # 도시 수 입력 (노드)
m = int(input())                                        # 버스 수 입력 (간선)
g = [[] for _ in range(n + 1)]                          # 그래프 인접 리스트로 초기화
table = [INF] * (n + 1)                                 # 최단거리 테이블 무한으로 초기화

for i in range(m):
    dep, arr, cost = map(int, input().split())          # 출발, 도착, 비용 입력
    g[dep].append((arr, cost))                          # 인접 리스트 생성

dep_city, arr_city = map(int, input().split())          # 시작 노드, 도착 노드 입력

dijkstra(g, dep_city, table)                            # 다익스트라 실행

print(table[arr_city])                                  # 도착 노드 값으로 최단 거리 출력