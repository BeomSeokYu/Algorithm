import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcs = list(input().rstrip())
    n = int(input())
    s = input().rstrip()[1:-1]
    arr = s.split(',') if s else []
    q = deque(arr)
    is_front = True
    flag = True
    for f in funcs:
        if f == 'R':
            is_front = False if is_front else True
        elif f == 'D':
            if len(q) < 1:
                print('error')
                flag = False
                break
            if is_front:
                q.popleft()
            else:
                q.pop()
    if flag:
        print('[', end='')
        if not is_front:
            q.reverse()
        print(*q, sep=',', end='')
        print(']')