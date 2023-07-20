import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
q = deque()
for _ in range(K):
    num = int(input())
    if num == 0:
        q.pop()
    else:
        q.append(num)
print(sum(q))