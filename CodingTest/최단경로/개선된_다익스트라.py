import sys, heapq # heapq 추가
input = sys.stdin.readline
INF = int(1e9)   # 무한을 의미하는 값으로 10억 상수 선언

# 노드의 개수 n, 간선의 개수 m
n, m = map(int, input().split())
# 시작 노드 번호 start
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 방문한 적이 이쓴ㄴ지 체크하는 목적의 리스트 만들기
# visited = [False] * (n + 1) # 우선순위 큐를 통해 확인 가능해 졌으므로 제거
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드의 인접 노드 b의 간선 가중치 c
    graph[a].append((b, c))

def dijkstra(start):
    # 우선순위 큐(최소힙)로 사용 될 리스트 선언
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드를 확인
        for i in graph[now]:
            cost = distance[now] + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우 무한(INFINITY)이라고 출력
    # 도달할 수 있는 경우 거리를 출력
    print('INFINITY') if distance[i] == INF else print(distance[i])