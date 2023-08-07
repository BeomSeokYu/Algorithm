import sys, heapq
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(q, (abs(num), num))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])