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

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    p = [q for q in range(n+1)]            # 부모 테이블 초기화
    cnt = 0
    for j in range(m):
        a, b = map(int, input().split())
        if find(p, a) != find(p, b):
            union(p, a, b)
            cnt += 1
    print(cnt)
