import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n:행 / mㅣ열
minList = []                        # 행에서 가장 작은 수를 담는 리스트
for i in range(n):
    row = list(map(int, input().split()))   # 행 입력
    minList.append(min(row))                # 행에서 가장 작은 수 담기
print(max(minList)) # 가장 작은 수들 중 가장 큰 수 출력