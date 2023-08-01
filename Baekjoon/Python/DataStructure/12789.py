import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque(list(map(int, input().split())))
stack = deque()
result = True
order = 1
while q or stack:
    if len(q) > 0 and q[0] == order:
        q.popleft()
        order += 1
    elif len(stack) > 0 and stack[-1] == order:
        stack.pop()
        order += 1
    else:
        if len(stack) == 0 or len(stack) > 0 and stack[-1] > q[0]:
            stack.append(q.popleft())
        else:
            result = False
            break
if result:
    print('Nice')
else:
    print('Sad')