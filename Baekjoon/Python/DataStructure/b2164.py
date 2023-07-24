import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque(list(range(1, N + 1)))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])