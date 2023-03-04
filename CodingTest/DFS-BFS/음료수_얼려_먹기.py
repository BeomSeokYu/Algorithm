# 얼음틀 크기 입력 받음
n, m = map(int, input().split())

# 얼음틀 입력 받음
iceFrame=[]
for i in range(n):
	iceFrame.append(list(map(int, input())))

# dfs
def dfs(graph, x, y):
	# 탐색 범위를 벗어났다면 종료
	if x < 0 or x >= n or y < 0 or y >= m:
		return False
	if graph[x][y] != 1:    # 해당 노드에 방문하지 않았으면
		graph[x][y] = 1       # 해당 공간을 막음으로 방문 처리

		dfs(graph, x+1, y)    # 상, 하, 좌, 우 재귀로 체크 연결 체크
		dfs(graph, x, y+1)
		dfs(graph, x-1, y)
		dfs(graph, x, y-1)
		return True           # 아이스크림 공간 있음
	return False            # 아이스크림 공간 없음 (막힘)

# 가능한 아이스크림 공간 갯수 세기
cnt = 0
for i in range(n):
	for j in range(m):
		if dfs(iceFrame, i, j):
			cnt += 1
print(cnt)                # 갯수 출력