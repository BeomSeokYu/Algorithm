import sys, math
input = sys.stdin.readline

# 루트 노드 찾기 함수
def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

# 두 노두 루트 노드 작은 수로 합치기
def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n = int(input())                            # 노두 갯수 입력
parent = [i for i in range(n+1)]            # 부모 테이블 초기화
stars = [0]                                 # 0번 인덱스 버림 별좌표 입력 받을 리스트

for i in range(1, n+1):
    x, y = map(float, input().split())
    stars.append((i, x, y))                 # 노드 번호와 좌표를 리스트에 삽입

dist = []                                   # 별 사이 거리(간선) 받을 리스트
for i in range(1, n):                       # 별 사이 간 거리를 하나씩 비교해 피타고라스 정리로 거리 구하기
    for j in range(i+1, n+1):
        cost = math.sqrt(abs(stars[i][1]-stars[j][1]) ** 2 + abs(stars[i][2]-stars[j][2]) ** 2)
        dist.append((cost, i, j))           # 별 사이 거리와 연결된 노드 두개 삽입
dist.sort()                                 # 거리로 오름차순 정렬

result = 0                                          # 총 비용 계산 결과 담을 변수
for i in dist:                                      # 거리가 짧은 순서대로
    if find(parent, i[1]) != find(parent, i[2]):    # 루트노드가 같지 않은 노드들에 대해(사이클이 없는 노드)
        union(parent, i[1], i[2])                   # 합치기
        result += i[0]                              # 총 비용 누적
print(result)                                       # 결과 출력
