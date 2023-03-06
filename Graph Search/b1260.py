import sys
from collections import deque           # deque 라이브러리 사용
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True                   # 방문 처리
    dfsSearch.append(v)                 # 탐색 리스트에 삽입

    graph[v].sort()                     # 인접 정점 리스트 오름차순으로 정렬
    for u in graph[v]:                  # 인접 정점 순환
        if not visited[u]:              # 방문하지 않은 정점이면
            dfs(graph, u, visited)      # 재귀로 방문 -> (스택과 같음)

# bfs 함수
def bfs(graph, v, visited):
    q = deque()                         # 큐 초기화
    visited[v] = True                   # 시작 정점 방문 처리
    q.append(v)                         # 시작 정점 큐에 삽입

    while q:                            # 큐가 빌때까지 반복
        node = q.popleft()              # 큐에서 하나 가져옴
        bfsSearch.append(node)          # 탐색 리스트에 삽입
        graph[node].sort()              # 인접 정점 리스트 오름차순으로 정렬
        for u in graph[node]:           # 인접 정점들 순환
            if not visited[u]:          # 인접 정점에 방문하지 않았다면
                q.append(u)             # 큐에 삽입
                visited[u] = True       # 방문 처리


n, m, v = map(int, input().split())     # n:정점 수, m:간선 수, v:정점 번호
graph = [[] for i in range(n+1)]        # 0부터라서 +1 (0번은 버림)
for _ in range(m):                      # 간선 수 만큼 입력
    a, b = map(int, input().split())    # 정점 a, b가 간선으로 이어져있음을
    graph[a].append(b)                  # 해당 정점 인덱스에 연결된 정점을 삽입해 입력
    graph[b].append(a)                  # (인접 리스트 방식)

dfsSearch = []                          # dfs 탐색 순서를 저장할 리스트
bfsSearch = []                          # bfs 탐색 순서를 저장할 리스트

visited = [False] * (n + 1)             # visited를 정점 수만큼 초기화 (0부터라서 +1)
dfs(graph, v, visited)                  # dfs 실행
visited = [False] * (n + 1)             # 다시 초기화
bfs(graph, v, visited)                  # bfs 실행

print(*dfsSearch, sep=' ')              # 출력
print(*bfsSearch, sep=' ')