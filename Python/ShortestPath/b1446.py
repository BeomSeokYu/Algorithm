import sys, heapq
input = sys.stdin.readline
INF = int(1e9)                                          # 무한 상수

def dijkstra(g, s, table):
    q = []
    heapq.heappush(q, (0, s))                           # 우선 순위 큐 시작 노드 초기화
    table[s] = 0                                        # 최단 거리 테이블 시작 노드 초기화

    while q:                                            # 큐가 빌 때까지 반복 수행
        c, now = heapq.heappop(q)                       # 큐에서 거리, 노드를 거리 최솟값으로 가져옴
        if table[now] < c:                              # 테이블이 더 작으면 이미 처리된 노드임 다음으로
            continue
        for node in g[now]:                             # 인접 노드들을 돌면서
            cost = node[1] + table[now]                 # 인접 노드의 거리를 더해 비용을 계산
            if cost < table[node[0]]:                   # 비용이 테이블보다 더 작으면
                table[node[0]] = cost                   # 테이블 갱신
                heapq.heappush(q, (cost, node[0]))      # 큐에 삽입

# 시작
n, d = map(int, input().split())                        # 지름길 갯수, 고속도로 길이 입력

g = [[] for i in range(10001)]                          # 최대 0 ~ 10000개 노드
for i in range(10000):
    g[i].append((i + 1, 1))                             # 각 0 ~ 10000을 노드로 보고 그래프 생성
table = [INF] * (10001)                                 # 초기 테이블 생성 및 무한으로 초기화

for i in range(n):
    dep, arr, length = map(int, input().split())        # 시작  위치, 도착 위치, 지름길 길이 입력
    g[dep].append((arr, length))                        # 위에서 만든 그래프에 간선 추가

dijkstra(g, 0, table)                                   # 다익스트라 수행

print(table[d])                                         # 도착 지점 최단 거리 출력