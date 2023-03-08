import sys
from collections import deque
input = sys.stdin.readline

adj = [(-2, 1),(-2, -1),                                        # 체스 말의 인접 정점 이동 리스트
       (-1, 2),(-1, -2),
       (1, 2),(1, -2),
       (2, 1),(2, -1)]

# bfs 함수
def bfs(g, x, y, blen):
    q = deque()                                                 # 큐 생성
    g[x][y] = 0                                                 # 시작 정점 거리 0
    q.append((x, y))                                            # 큐에 시작 정점 좌표 삽입

    while q:                                                    # 큐가 빌때까지 반복
        x, y = q.popleft()                                      # 큐에서 하나 뽑음
        for ax, ay in adj:                                      # 다음 정점으로 이동해야할 위치들
            rx, ry = (x + ax), (y + ay)                         # 다음 정점 위치
            if rx < 0 or ry < 0 or rx >= blen or ry >= blen:    # 범위 내에 존재하지 않으면
                continue                                        # 다음거 확인
            if g[rx][ry] == -1:                                 # 방문 안한 정점이면
                q.append((rx, ry))                              # 큐에 삽입
                g[rx][ry] = g[x][y] + 1                         # 거리 현 위치에 +1
    return g

for _ in range(int(input())):                                   # 테스트 케이스 만큼 반복
    blen = int(input())                                         # 가로 세로 길이
    sx, sy = map(int, input().split())                          # 시작 위치
    ex, ey = map(int, input().split())                          # 도착해야 할 위치
    g = [([-1] * blen) for _ in range(blen)]                    # 그래프 -1로 2차원 배열 생성
    g = bfs(g, sx, sy, blen)                                    # bfs 실행
    print(g[ex][ey])                                            # 도착 위치 거리 출력
