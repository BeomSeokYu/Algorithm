import sys
input = sys.stdin.readline

for _ in range(int(input())):
    rank = []
    n = int(input())
    for _ in range(n):
        rank.append(list(map(int, input().split())))
    rank.sort(key=lambda x : x[0])
    cnt = 1
    _max = rank[0][1]
    for i in range(1, n):
        if rank[i][1] < _max :
            cnt += 1
            _max = rank[i][1]
            continue
    print(cnt)