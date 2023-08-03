from collections import deque

N = int(input())
li = list(map(int, input().split()))
q = deque()
result = []
for i in range(len(li)):
    q.append((i + 1, li[i]))
while True:
    num, move = q.popleft()
    result.append(num)
    if not q:
        break
    if move > 0:
        for j in range(abs(move) - 1):
            q.append(q.popleft())
    else:
        for k in range(abs(move)):
            q.appendleft(q.pop())

print(*result, sep=' ')