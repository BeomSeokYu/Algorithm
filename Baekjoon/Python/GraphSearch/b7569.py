import sys
from collections import deque

input = sys.stdin.readline

def bfs(V, H, N, M):
    q = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if V[h][n][m] == 1:
                    q.append((h, n, m))
                    V[h][n][m] = 2
    while q:
        h, n, m = q.popleft()
        for nn, nm, nh in [(n + 1, m, h), (n - 1, m, h), (n, m + 1, h), (n, m - 1, h), (n, m, h + 1), (n, m, h - 1)]:
            if  nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if V[nh][nn][nm] == -1:
                continue
            if V[nh][nn][nm] == 0 or V[nh][nn][nm] > V[h][n][m] + 1:
                V[nh][nn][nm] = V[h][n][m] + 1
                q.append((nh, nn, nm))

M, N, H = map(int, input().split()) # M:가로, N:세로
V = []

for i in range(H):
    V.append([])
    for j in range(N):
        V[i].append(list(map(int, input().split())))

bfs(V, H, N, M)

result = 0
for h in range(H):
    for n in range(N):
        if V[h][n].count(0) > 0:
            result = -1
            break
        else:
            result = max(max(V[h][n]), result)
    if result == -1:
        break

print(result) if result == -1 else print(result - 2)