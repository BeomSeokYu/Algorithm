import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()
for i in range(N):
    ins = input().rstrip().split()
    if ins[0] == 'push_front':
        q.appendleft(ins[1])
    elif ins[0] == 'push_back':
        q.append(ins[1])
    elif ins[0] == 'pop_front':
        print(q.popleft()) if len(q) != 0 else print(-1)
    elif ins[0] == 'pop_back':
        print(q.pop()) if len(q) != 0 else print(-1)
    elif ins[0] == 'size':
        print(len(q))
    elif ins[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif ins[0] == 'front':
        print(q[0]) if len(q) != 0 else print(-1)
    elif ins[0] == 'back':
        print(q[-1]) if len(q) != 0 else print(-1)