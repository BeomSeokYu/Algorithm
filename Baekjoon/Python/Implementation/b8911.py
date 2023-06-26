'''
거북이의 이동은 F, B로만 이루어 진다.
이동 방향은 y, x, -y, -x 네 방향이다.
이동 방향 별로 이동한 최대 이동 거리를 기록해야 한다.
'''

import sys
input = sys.stdin.readline

# 바라 보는 방향 별 축과 이동 정리를 담은 딕셔너리
moveDic = {0:['y', 1], 1:['x', 1], 2:['y', -1],3:['x', -1]}

# 이동 처리와 이동 최대 최솟값 저장
def move(x, y, direc, xyMax):
    moveInfo = moveDic[direc]
    if moveInfo[0] == 'y':
        y += moveInfo[1]
        xyMax[0] = max(xyMax[0], y)
        xyMax[2] = min(xyMax[2], y)
    else:
        x += moveInfo[1]
        xyMax[1] = max(xyMax[1], x)
        xyMax[3] = min(xyMax[3], x)
    return x, y, xyMax

for i in range(int(input())):   # 테스트 케이스
    x, y = 0, 0             # 위치 저장
    xyMax = [0, 0, 0, 0]    # 방향별 최대 이동 거리 저장
    direc = 0               # 방향 - 0:상, 1우, 2:하, 3:좌

    for i in input().rstrip():  # 1~500
        if i == 'F':
            x, y, xyMax = move(x, y, direc, xyMax)
        elif i == 'B':
            revDir = direc + 2 if direc < 2 else direc - 2
            x, y, xyMax = move(x, y, revDir, xyMax)
        elif i == 'L': # 왼쪽 방향 전환
            direc -= 1
            if direc < 0:
                direc = 3
        elif i == 'R': # 오른쪽 방향 전환
            direc += 1
            if direc > 3:
                direc = 0
    print(abs(xyMax[0] - xyMax[2]) * abs(xyMax[1] - xyMax[3])) #좌표 직사각형 넓이 구하기