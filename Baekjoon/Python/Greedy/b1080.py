'''

'''

import sys
input = sys.stdin.readline

# 3*3 영역의 행렬을 뒤집어 반환하는 함수
def reverseMat(i, j, mat):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            mat[x][y] = 1 if mat[x][y] == 0 else 0
    return mat

# n * m 행렬
n, m = map(int, input().split())
matA, matB = [], []
for mat in matA, matB: # 행렬 a, b 차례로 입력
    for j in range(n):
        mat.append(list(map(int, list(input().rstrip()))))

#print(matA)
#print(matB)

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if matA[i][j] != matB[i][j]: #두 행렬의 각 숫자 하나씩을 비교하면서 다른 경우 다음 아래의 3*3영역을 뒤집음
            matA = reverseMat(i, j, matA)
            cnt += 1                 # 횟수 카운트
#print(matA)
#print(matB)

print(-1) if matA != matB else print(cnt) # 두 행렬이 다르면 -1 같으면 횟수 출력