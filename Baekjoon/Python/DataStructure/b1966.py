import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))
    result = 0
    while True:
        if q[0] != max(q):
            q.append(q.popleft())
        else:
            q.popleft()
            result += 1
            if M == 0:
                break
        M -= 1
        if M < 0:
            M = len(q) - 1
    print(result)