import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
target = deque()
_max = 0
isTrue = True
answer = []

for _ in range(n):
    num = int(input())
    if num > _max:
        for i in range(_max + 1, num + 1):
            target.append(i)
            answer.append('+')
        target.pop()
        answer.append('-')
        _max = num
    elif len(target) > 0 and target[-1] == num:
        target.pop()
        answer.append('-')
    else:
        isTrue = False
if isTrue:
    print(*answer, sep="\n")
else:
    print("NO")