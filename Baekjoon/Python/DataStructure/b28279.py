import sys
from collections import deque
input = sys.stdin.readline

q = deque()
N = int(input())
for _ in range(N):
    inst = list(map(int, input().split()))
    if inst[0] == 1:
        q.appendleft(inst[1])
    elif inst[0] == 2:
        q.append(inst[1])
    elif inst[0] == 3:
        print(q.popleft()) if len(q) > 0 else print(-1)
    elif inst[0] == 4:
        print(q.pop()) if len(q) > 0 else print(-1)
    elif inst[0] == 5:
        print(len(q))
    elif inst[0] == 6:
        print(1) if len(q) == 0 else print(0)
    elif inst[0] == 7:
        print(q[0]) if len(q) > 0 else print(-1)
    elif inst[0] == 8:
        print(q[-1]) if len(q) > 0 else print(-1)
