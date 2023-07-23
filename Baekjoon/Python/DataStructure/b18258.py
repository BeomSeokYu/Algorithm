import sys
from collections import deque
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    op = input().rstrip()
    if op.split()[0] == 'push':
        q.append(op.split()[1])
    elif op == 'pop':
        print(q.popleft()) if len(q) > 0 else print(-1)
    elif op == 'size':
        print(len(q))
    elif op == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif op == 'front':
        print(q[0]) if len(q) > 0 else print(-1)
    elif op == 'back':
        print(q[-1]) if len(q) > 0 else print(-1)