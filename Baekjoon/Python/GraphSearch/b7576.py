import sys
from collections import deque

input = sys.stdin.readline

def bfs(V, N, M):
    q = deque()
    for n in range(N):
        for m in range(M):
            if V[n][m] == 1:
                q.append((n, m))
                V[n][m] = 2
    while q:
        n, m = q.popleft()
        for nn, nm in [(n + 1, m), (n - 1, m), (n, m + 1), (n, m - 1)]:
            if nn >= 0 and nn < N and nm >= 0 and nm < M:
                if V[nn][nm] == -1:
                    continue
                if V[nn][nm] == 0 or V[nn][nm] > V[n][m] + 1:
                    V[nn][nm] = V[n][m] + 1
                    q.append((nn, nm))

M, N = map(int, input().split()) # M:가로, N:세로
V = []

for i in range(N):
    V.append(list(map(int, input().split())))

bfs(V, N, M)

result = 0
for n in range(N):
    if V[n].count(0) > 0:
        result = -1
        break
    else:
        result = max(max(V[n]), result)

print(result) if result == -1 else print(result - 2)

# 커밋 메시지 수정용 메시지