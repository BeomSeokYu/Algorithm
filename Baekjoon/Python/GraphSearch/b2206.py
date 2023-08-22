import sys, copy
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

isWall = False

def bfs(G, N, M):
    G[0][0][0] = 1
    qq = deque()
    qq.append(deque([(0, 0)]))
    rflag = True
    while qq:
        q = qq.popleft()
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x - dx[i], y - dy[i]
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
                    continue
                if G[-1][ny][nx] == 0 or G[-1][ny][nx] > G[-1][y][x] + 1:
                    G[-1][ny][nx] = G[-1][y][x] + 1
                    q.append((nx, ny))
                elif G[-1][ny][nx] == 1 and rflag:
                    for i in range(4):
                        nnx, nny = nx - dx[i], ny - dy[i]
                        if nnx < 0 or nny < 0 or nnx >= M or nny >= N:
                            continue
                        if G[-1][nny][nnx] == 0:
                            ng = copy.deepcopy(G[0])
                            ng[ny][nx] = ng[y][x] + 1
                            nq = copy.deepcopy(q)
                            nq.append((nx, ny))
                            qq.append(nq)
                            G.append(ng)
                            break
        rflag = False

N, M = map(int, input().split())
G = [[]]
for i in range(N):
    str = input().rstrip()
    temp = []
    for s in str:
        temp.append(int(s))
    G[0].append(temp)

bfs(G, N, M)

result = 0
for i in range(len(G)):
    result = max(G[i][-1][-1], result)
print(result if result != 0 else -1)