import sys
input = sys.stdin.readline

n = int(input())
hanzos = list(map(int, input().split()))

kill, maxkill = 0, 0    # 한조가 죽인 한조들과, 그 최댓값을 저장하는 변수
strong = hanzos[0]      # 첫번째 산 한조 강한놈으로 지정
for i in range(1, len(hanzos)): # 한조들 반복
    if hanzos[i] > strong:      # 다른 한조가 더 강하면 바꿈
        strong = hanzos[i]
        kill = 0                # 킬 초기화
    else:
        kill += 1               # 나보다 약하면 죽여버림
        if kill > maxkill:      # 킬수가 가장 높다면 저장
            maxkill = kill
print(maxkill)                  # 가장 높은 킬 출력