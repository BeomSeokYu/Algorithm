import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

if len(li) > 2:

    d = [0] * n                                 # DP 테이블

    d[0] = li[0]                                # 첫 계단
    d[1] = li[0] + li[1]                        # 두 번째 계단
    d[2] = max(li[1] + li[2], li[0] + li[2])    # 세 번째 까지 수동 계산
    for i in range(3, n):
        d[i] = max(d[i - 3] + li[i - 1] + li[i], d[i - 2] + li[i])
        # 3개 전 계단 dp 테이블과 전 계단의 값, 현재 값의 합과
        # 2개 전 계단 dp 테이블과 현재 계단의 값 중 큰 것 선택의 현재 dp 테이블에 기록
        # 점화식 : a(i) = max(a(i-3) + k(i-1) + k(i), a(i-2) + k(i))

    print(d[n - 1])
else:                                   # 개단이 2개 이하면
    print(sum(li))                      # 그냥 더해서 출력함 (인덱스 오류..)