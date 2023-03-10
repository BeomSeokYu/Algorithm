import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, s, visited):             # g: 그래프 / s: 시작 정점 / visited: 방문 리스트
    result = 0                      # 감염 컴퓨터 수 셀 변수

    q = deque()                     # 큐 선언
    visited[s] = True               # 시작 정점 방문 처리
    q.append(s)                     # 큐에 삽입

    while q:                        # 큐 빌때까지
        v = q.popleft()             # 큐에서 하나 가져와서
        for u in g[v]:              # 인접 정점 다 돌면서
            if not visited[u]:      # 방문 안한 정점이면
                visited[u] = True   # 방문 처리
                q.append(u)         # 큐 삽입
                result += 1         # 감염 컴퓨터 +1
    return result                   # 결과 반환

n = int(input())                    # 컴퓨터 수
g = [[] for i in range(n + 1)]      # 그래프 담을 리스트, 인덱스 맞추려고 +1
visited = [False] * (n + 1)         # 방문 리스트

for i in range(int(input())):       # 인접 리스트 방식으로 기록
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

print(bfs(g, 1, visited))           # bfs 결과 출력