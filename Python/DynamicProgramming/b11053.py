import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [1] * (n + 1)                       # 인덱스 맞춤

for i in range(n):                      # i가 선택한 값이면
    for j in range(i):                  # i 이전 값 중에
        if arr[i] > arr[j]:             # i 보다 작은거 있으면
            d[i] = max(d[i], d[j] + 1)  # dp테이블 값에 +1 한거랑 비교해 큰 값 저장
_max = max(d)                           # 가장 긴 값을 선택
print(_max)