import sys, heapq
input = sys.stdin.readline
INF = int(1e9)                              # 초기 무한 설정용 상수

prob = 0                                    # 테스트 케이스 문제 번호
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 좌, 상, 우, 하

# 다익스트라 함수
def dijkstra(g, x, y, sp, n):
    q = []                                  # 우선순위 큐로 쓸거임
    heapq.heappush(q, (g[0][0], x, y))      # 초기 비용 우선순위로 비용과 값으로 x, y좌표 푸쉬
    sp[0][0] = g[0][0]                      # 테이블에 시작 노드 초기값 설정

    while q:                                # 큐가 빌 때까지 반복 수행
        d, x, y = heapq.heappop(q)          # 최소 비용 하나 가져와 봄

        if sp[x][y] < d:                    # 큐에 값이 테이블 보다 더 크면 이미 계산된 것이므로 패스
            continue
        for rx, ry in dir:                  # 노드의 4방향 탐색
            rx += x
            ry += y
            if rx >= 0 and rx < n and ry >= 0 and ry < n:   # 범위를 벗어나지 않았다면
                cost = sp[x][y] + g[rx][ry]                 # 현재 값에 다음 값을 더해 비용 계산
                if cost < sp[rx][ry]:                       # 최저 값이면
                    sp[rx][ry] = cost                       # 테이블 갱신
                    heapq.heappush(q, (cost, rx, ry))       # 큐 삽입
    return sp


while True:
    # 문제 번호
    prob += 1

    # 크기 입력
    n = int(input())
    # 0 입력 시 종료
    if n == 0:
        break

    # 우선순위 테이블
    sp = [[INF] * n for _ in range(n)]

    # 그래프 입력
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))

    # 다익스트라 결과 최단거리 출력
    print("Problem %d: %d" % (prob, dijkstra(g, 0, 0, sp, n)[n-1][n-1]))