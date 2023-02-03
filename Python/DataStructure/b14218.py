'''
도시의 개수 n
도로의 개수 m
도로 정비 계획에 들어가 있는 도로의 수 q
1이 수도

도시 번호를 어떻게 기억할 것인가?
bfs를 써야되는데..?

dp 메모이제이션?
'''

import sys
input = sys.stdin.readline

# 최단 거리 무식하게 찾는 함수
def findRoute(result, cityRoute, i, j):
    if(i == 1):
        result[j] = 1 # 수도와 연결된 도시 최단 거리 설정
    elif result[i] != -1 and result[j] != -1: # 둘다 수도와 연결된 노드가 없을 경우
        if result[j] > result[i]:             # 더 작은 쪽에 +1
            result[j] = result[i] + 1
        elif result[j] < result[i]:
            result[i] = result[j] + 1
    elif result[i] == -1 and result[j] != -1: # 한쪽에만 수도와 연결되어 있을 경우
        result[i] = result[j] + 1             # 연결 안된 도시는 연결된 도시의 +1
        for k in cityRoute[i]:                # 연결 안된 도시와 연결된
            if k == -1:                       # 또 다른 연결 안된 도시들에 대해
                result[k] = result[i] + 1     # 연결 안된 도시는 연결된 도시의 +1
    elif result[i] != -1 and result[j] == -1: # 연결 안된 도시들이 길게 연결 되었을 경우 상행 방향으로만 최단 거리가 계산 되므로 하행식도 필요하게 됨...
        result[j] = result[i] + 1             # => bfs를 구현해 쓸 줄 알아야 됨.
        for k in cityRoute[j]:
            if k == -1:
                result[k] = result[j] + 1

# 도시간 경로 입력 함수
def inputRoute():
    a, b = map(int, input().split())
    cityRoute[a].append(b)
    cityRoute[b].append(a)


n, m = map(int, input().split())

result = [-1] * (n + 1) # 각 도시의 최단거리 저장. 수도가 1부터인 인덱스를 맞추기 위해 +1
result[1] = 0           # 수도의 경로는 0
cityRoute = {}          # 각 노드(키)가 연결된 노드 리스트를 갖는 딕셔너리
for i in range(1, n+1):
    cityRoute[i] = []   # 빈 리스트 도시별로 추가

for _ in range(m):
    inputRoute()        # 기존 도로를 입력 받아 딕셔니리에 도로별로 삽입

q = int(input())
for _ in range(q):
    inputRoute()        # 새로 연결되는 도로를 입력 받아 딕셔니리에 도로별로 삽입

    # 1번 도시부터 상향식으로 한 번 루트를 돌며 최단 거리를 찾음
    for i in cityRoute:
        for j in cityRoute[i]:
            findRoute(result, cityRoute, i, j)
    # n번 도시부터 하향식으로 한 번 루트를 돌며 최단 거리를 찾음
    for i in sorted(cityRoute.keys(), reverse=True):
        for j in cityRoute[i]:
            findRoute(result, cityRoute, i, j)
    # 도시별 최단 거리 출력
    for i in range(1, n+1):
        print(result[i], end=" ")
    print()