import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, x, y):
    q = deque()                                         # 큐 생성
    q.append((x, y))                                    # 시작 지점 삽입

    while q:                                            # 큐 빌때까지 반복
        vx, vy = q.popleft()                            # 큐에 있는 위치 빼기
        for d in dir:                                   # 그 위치에서 상하좌우 확인
            dx, dy = dir[d]                             # 상하좌우 위치 이동 값 딕셔너리에서 하나 뺌
            rx = vx + dx                                # 현재 위치에서 이동한 새 좌표
            ry = vy + dy
            if rx < 0 or ry < 0 or rx >= n or ry >= m:  # 그 좌표가 범위를 벗어난 좌표면 되돌아감
                continue
            if g[rx][ry] == 1:                          # 범위 안에 있고 값이 1이면
                q.append((rx, ry))                      # 큐에 넣고
                g[rx][ry] = g[vx][vy] + 1               # 그 값에 +1 해서 거리 값을 넣어줌
    return g[n-1][m-1]                                  # 다 돌고 나서 마지막 위치에 있는 값(거리) 반환

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))        # 2차원 배열 형태의 미로 입력 받음

dir = {                                                 # 방향 관련 딕셔너리 (내가 보기 좋음 ㅎ)
    'u': (0, 1),
    'd': (0, -1),
    'l': (-1, 0),
    'r': (1, 0)}
print(bfs(maze, 0, 0))                                  # 결과 출력