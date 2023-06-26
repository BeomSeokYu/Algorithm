import sys
input = sys.stdin.readline
INF = int(1e9)


# 도시 수
n = int(input())
# 버스 수
m = int(input())

# 2차원 리스트 최단 거리 테이블을 만들고, 모든 값을 무한으로 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신으로 가는 값은 0으로 입력
for i in range(1, n + 1):
    dist[i][i] = 0

# a 에서 b 로가는 값 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)         # 조건 : 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 플루이드 워셜 실행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j], end=" ") if dist[i][j] != INF else print(0, end=" ")
    print()