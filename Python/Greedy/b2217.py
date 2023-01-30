'''

'''

import sys
input = sys.stdin.readline

lw = []
n = int(input())

for i in range(n):
	lw.append(int(input()))
lw.sort()

for i in range(n):
	lw[i] *= (n - i)
print(sorted(lw)[-1])
