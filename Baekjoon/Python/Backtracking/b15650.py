'''
7 4
1 2 3 4
1 2 3 5
1 2 3 6
1 2 3 7
1 2 4 5
1 2 4 6
1 2 4 7
1 2 5 6
1 2 5 7
1 2 6 7
1 3 4 5
1 3 4 6
1 3 4 7
1 3 5 6
1 3 5 7
1 3 6 7
1 4 5 6
1 4 5 7
1 4 6 7
1 5 6 7
2 3 4 5
2 3 4 6
2 3 4 7
2 3 5 6
2 3 5 7
2 3 6 7
2 4 5 6
2 4 5 7
2 4 6 7
2 5 6 7
3 4 5 6
3 4 5 7
3 4 6 7
3 5 6 7
4 5 6 7
'''

import sys
input = sys.stdin.readline

def move_cursor(cursor, N, idx):
    if idx < 0:
        return False
    if idx == len(cursor) - 1:  # 마지막 커서일 경우
        if cursor[idx] < N - 1:
            cursor[idx] += 1
        else:
            return move_cursor(cursor, N, idx - 1)
    else:                       # 마지막 커서가 아닐 경우
        if cursor[idx] < cursor[idx + 1] - 1:
            cursor[idx] += 1
            for i in range(idx + 1, len(cursor)):   # 변경이 생기면 이후 커서들을 현재 커서에 순차적으로 배치
                cursor[i] = cursor[idx] + i - idx
        else:
            return move_cursor(cursor, N, idx - 1)
    return True

N, M = map(int, input().split())
li = [i for i in range(1, N + 1)]
cursor = [j for j in range(M)]

while True:
    for i in cursor:
        print(li[i], end=" ")
    print("")
    if (not move_cursor(cursor, N, M - 1)):
        break