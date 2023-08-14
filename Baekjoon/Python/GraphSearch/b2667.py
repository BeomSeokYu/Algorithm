import sys

input = sys.stdin.readline

def dfs(V, x, y, result):
    V[x][y] = 2
    result[-1] += 1
    for rx, ry in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if rx >= 0 and rx < N and ry >= 0 and ry < N:
            if V[rx][ry] == 1:
                dfs(V, rx, ry, result)

N = int(input())
V = [[] for _ in range(N)]

for i in range(N):
    str = input().rstrip()
    for j in str:
        V[i].append(int(j))

result = []
for i in range(N):
    for j in range(N):
        if V[i][j] == 1:
            result.append(0)
            dfs(V, i, j, result)

result.sort()
print(len(result))
print(*result, sep='\n')