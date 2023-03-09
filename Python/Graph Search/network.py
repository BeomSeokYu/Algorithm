def solution(n, computers):
    answer = 0
    visited = [False] * n
    adjList = [[] for _ in range(n)]

    # 인접 리스트로 변환 (인접 행렬로 어떻게 풀어야 할지 감이 안오네..)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                adjList[i].append(j)
    print(adjList)

    for i in adjList:
        for j in i:
            if not visited[j]:              # 모든 접점 방문 했는지 검사하면서 dfs 실행
                dfs(adjList, j, visited)
                answer += 1                 # dfs에서 인접 노드들은 모드 방문해 한 트리가 형성됨 고로 +1
    return answer

def dfs(g, v, visited):                     # dfs 실행 함수
    visited[v] = True                       # 방문 처리
    for i in g[v]:                          # 인접 노드들에 대해
        if not visited[i]:                  # 방문 안했으면
            dfs(g, i, visited)              # 그 노드에 대해 다시 dfs

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 테스트용 코드