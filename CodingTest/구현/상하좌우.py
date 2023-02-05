import sys
input = sys.stdin.readline

n = int(input())            # 공간 크기 입력
planer = input().split()    # 이동 계획 입력

# 이동 계획에 따라 (이동 축, 이동 방향)을 같는 딕셔너리
mapPlan = {'L':(1, -1), 'R':(1, 1), 'U':(0, -1), 'D':(0, 1)}
# 현재 좌표
coor = [1, 1]
# 이동 계획을 하나씩 수행
for i in planer:
    t = mapPlan[i]              # 이동 축, 이동 방향을 가져옴
    temp = coor[t[0]] + t[1]    # 이동 축에서 이동 방향으로 이동한 결과
    if temp > 0 and temp <= n:  # 범위를 벗어나지 않았다면
        coor[t[0]] = temp       # 현재 좌표에 적용
print(coor[0], coor[1])         # 최종 출력