import sys
from collections import deque
input = sys.stdin.readline

def topology_sort(g, n, indegree, time):
    result = time[:]                                            # 사용할 시간 배열 복사
    q = deque()

    for i in range(1, n + 1):                                   # 초기 진입차수가 0인 노드들 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()                                       # 큐에서 하나 꺼내
        for i in g[now]:                                        # 후수과목 순환
            result[i] = max(result[i], result[now] + time[i])   # 인접 노드에 대해 현재보다 강의 시간이 더 긴 경우를 찾음 (더 오랜 시간이 걸리는 경우 갱신)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

n = int(input())
indegree = [0] * (n + 1)
g = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp.pop(0)
    temp.remove(-1)
    for j in temp:                                              # 인접 리스트와 진입차수 리스트 생성
        indegree[i] += 1
        g[j].append(i)

result = topology_sort(g, n, indegree, time)
for i in range(1, n + 1):
    print(result[i])