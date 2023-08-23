'''
일반적인 최단거리 출력 -> 이미 방문한 곳은 최단 거리가 아님 -> 방문 여부 체크가 중요
벽을 1개 부술수 있다면? -> 이미 방문한 곳이라도 벽을 부수고 방문했는지, 부수지 않고 방문했는지로 나뉨

- 벽을 부수고 난 후 방문한 경로가 이전에 방문한 경로라면 최단거리가 아니다
- 벽을 부수지 않았는데, 벽을 부순 경로가 이미 방문한 적이 있다면 방문 가능해야함

'''

import sys, copy
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(G, N, M):
    G[0][0][0] = 2
    is_broken = 0
    q = deque([(0, 0, is_broken)])
    while q:
        x, y, is_broken = q.popleft()
        for i in range(4):
            nx, ny = x - dx[i], y - dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if G[0][ny][nx] == 1 and is_broken == 0 and G[1][ny][nx] == 1:
                G[1][ny][nx] = G[0][y][x] + 1
                q.append((nx, ny, 1))
            elif G[is_broken][ny][nx] == 0:
                G[is_broken][ny][nx] = G[is_broken][y][x] + 1
                q.append((nx, ny, is_broken))

N, M = map(int, input().split())
G = [[],[]]
for i in range(N):
    str = input().rstrip()
    temp = []
    for s in str:
        temp.append(int(s))
    G[0].append(temp)
    G[1].append(copy.deepcopy(temp))

bfs(G, N, M)

result = 1000001
for i in range(len(G)):
    if G[i][-1][-1] == 0:
        G[i][-1][-1] = 1000001
    result = min(G[i][-1][-1], result)
print((result - 1) if result != 1000001 else -1)