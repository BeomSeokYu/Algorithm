import sys
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n, m = map(int, input().split())

p = [i for i in range(n + 1)]

edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
last_road = 0                               # 가장 큰 비용의 신장트리 길을 저장하기 위함
for c, a, b in edges:
    if find(p, a) != find(p, b):
        union(p, a, b)
        result += c
        last_road = c

print(result - last_road)                   # 가장 큰 비용의 신장트리 길을 없애 2개의 마을을 만듬