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
p = [0] * (n + 1)
for i in range(1, n + 1):
	p[i] = i

for i in range(m):
	op, a, b = map(int, input().split())
	if op == 0:
		union(p, a, b)
	else:
		print('YES') if find(p, a) == find(p, b) else print('NO')