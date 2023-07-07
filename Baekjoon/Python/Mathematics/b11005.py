# 진법 딕셔너리 생성
d = {}
for i in range(10):
    d[i] = str(i)
for i in range(ord('A'), ord('Z') + 1):
    d[i - 55] = chr(i)

# 입력 값
N, B = map(int, input().split())

# 계산
q = 0
result = []
while N > 0:
    q = N % B
    N = N // B
    result.insert(0, d[q])

# 출력
print(*result, sep='')