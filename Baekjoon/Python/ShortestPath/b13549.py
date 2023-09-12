import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s, dist):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i, c in ((now + 1, 1), (now - 1, 1), (now * 2, 0)):
            if i < 0 or i > 100000:
                continue
            cost = dist[now] + c
            if cost < dist[i]:
                dist[i] = cost
                heapq.heappush(q, (cost, i))

N, K = map(int, input().split())
dist = [INF] * (100001)
dijkstra(N, dist)
print(dist[K])