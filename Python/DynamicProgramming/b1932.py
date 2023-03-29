import sys
input = sys.stdin.readline

# 입력 및 삼각형 2차원 리스트로 초기화
n = int(input())
tr = []
for _ in range(n):
    tr.append(list(map(int, input().split())))

# 2차원 dp테이블 생성 및 최상단 값 초기화
d = [[0] * (n) for _ in range(n)]
d[0][0] = tr[0][0]

# 해당 인덱스 밑의 두 원소에 대해 dp테이블 갱신 실행
# 점화식
# 왼쪽      : a_{ij} = max(a_{(i+1)(j)}, a_{ij} + k_{(i+1)(j)})
# 오른쪽    : a_{(i)(j+1)} = max(a_{(i+1)(j+1)}, a_{ij} + k_{(i+1)(j+1)})
for i in range(n - 1):
    for j in range(len(tr[i])):
        d[i + 1][j] = max(d[i + 1][j], d[i][j] + tr[i + 1][j])
        d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + tr[i + 1][j + 1])

# 테이블 최 하단값 중 최댓값 출력
print(max(d[-1]))