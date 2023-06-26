from collections import deque

# 미로 크기 입력
n, m = map(int, input().split())
# 미로 정보 입력
maze = []
for i in range(n):
	maze.append(list(map(int, input())))

# 방향 정보 딕셔너리
dir = {'u': (-1, 0), 'd':(1, 0), 'l':(0, -1), 'r':(0, +1)}

# bfs
def bfs(graph, x, y):
	q = deque()
	q.append((x, y))        # 시작 위치 큐에 삽입
	graph[x][y] = 1         # 괴물 위치로 바꿔 방문 처리
	while q:                # 큐가 빌 때까지
		x, y = q.popleft()    # 큐에서 현재 위치 빼기
		for d in dir:         # 상, 하, 좌, 우 확인
			dx, dy = dir[d]     # 다음 위치 지정
			rx, ry = x + dx, y + dy
			# 미로 안에 없다면 다음 조건 진행
			if (rx < 0 or rx >=n or ry < 0 or ry >= m):
				continue
			# 값이 1이라면 (처음 위치는 재방문 하지만 상관없으므로 진행)		
			if graph[rx][ry] == 1:
				q.append((rx, ry))                # 큐에 다음 위치로 넣기
				graph[rx][ry] = graph[x][y] + 1   # 다음 위치의 거리로 현재 위치 거리에 + 1
	return graph[n-1][m-1]  # 마지막 위치에 거리를 반환

# 실행
print(bfs(maze, 0, 0))