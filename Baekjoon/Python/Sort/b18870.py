import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))     # 좌표 입력
sl = sorted(set(l))                     # 입력 좌표들 중복 제거 및 정렬

d = {}
idx = 0                                 # 압축된 좌표에 부여할 새 좌표
for i in sl:
    d[i] = idx                          # 각 좌표 당 압축된 새 좌표 부여
    idx += 1
for i in l:
    print(d[i], end=" ")                # 출력