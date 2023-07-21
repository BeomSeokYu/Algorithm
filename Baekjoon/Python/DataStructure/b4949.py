import sys
from collections import deque

input = sys.stdin.readline

while True:
    stack = deque()

    str = input().rstrip()
    if str == '.':
        break
    try:
        for i in str:
            if i in ('(', '['):
                stack.append(i)
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            elif i == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
    except IndexError:
        print('no')
        continue
    if len(stack) == 0 and len(stack) == 0:
        print('yes')
    else:
        print('no')