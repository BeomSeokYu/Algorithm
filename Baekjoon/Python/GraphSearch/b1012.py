import sys
from collections import deque
input = sys.stdin.readline

def bfs(V, y, x, M, N):
    V[y][x] = 2
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for rx, ry in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if rx >= 0 and rx < M and ry >= 0 and ry < N:
                if V[ry][rx] == 1:
                    V[ry][rx] = 2
                    q.append((rx, ry))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    V = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        V[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if V[i][j] == 1:
                result += 1
                bfs(V, i, j, M, N)

    print(result)