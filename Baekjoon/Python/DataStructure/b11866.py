import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
answer = []

q = deque(range(1, N + 1))
while q:
    for i in range(K - 1):
        q.append(q.popleft())
    answer.append(q.popleft())
print('<', end='')
print(*answer, sep=', ', end='')
print('>')