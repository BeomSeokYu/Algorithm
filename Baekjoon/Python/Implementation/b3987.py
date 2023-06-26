import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stellar = []
for _ in range(n):
    stellar.append(list(input().rstrip()))
pr, pc = map(int, input().split())

dirDic = {'U':[0, -1], 'R':[1, 1], 'D':[0, 1], 'L':[1, -1]}     # 방향 이동 정보
slashDic = {'U':'R', 'D':'L', 'R':'U', 'L':'D'}                 # / 방향 전환
backDic = {'U':'L', 'D':'R', 'R':'D', 'L':'U'}                  # \ 방향 전환

result = ['U', 0]
for i in dirDic:                            # 4가지 방향에 대해 거리 구하기 시작
    dist = 0                                # 초기 거리
    dir = i                                 # 초기 방향
    infinite = False                        # 무한 여부
    area = [n-1, m-1]                       # 공간 크기
    loc = [pr-1, pc-1]                      # 현재 위치
    while True:
        if stellar[loc[0]][loc[1]] == 'C':  # 블랙홀 만나면 바로 ㅂㅂ
            break
        elif stellar[loc[0]][loc[1]] == '/':      # 반향 전환
            dir = slashDic[dir]
        elif stellar[loc[0]][loc[1]] == '\\':
            dir = backDic[dir]

        dirInfo = dirDic[dir]               # 현재 방향의 이동 정보 가져오기
        loc[dirInfo[0]] += dirInfo[1]       # 현재 위치 변경
        dist += 1                           # 시간 증가

        if dist > (n * m * 2):              # 이거 보다 크면 갖힌거임 ㅅㄱ
            infinite = True
            break
        elif loc[dirInfo[0]] > area[dirInfo[0]] or loc[dirInfo[0]] < 0: # 계를 벗어나면 그만임
            break
    if infinite:                                # 무한대일 경우
        result = [i, 'Voyager']
        break                                   # 바로 종료
    elif result[1] < dist:                      # 아니면 거리가 큰 걸로 결과값 교체
        result = [i, dist]
print(*result, sep='\n')                        # 결과 출력