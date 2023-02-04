import sys
input = sys.stdin.readline
# 최대한 많이 나누기
n, k = map(int, input().split())
result = 0

while n != 1:           # n이 1이 될 때까지 반복
    if n % k == 0:      # k가 n의 배수이면
        n = int(n / k)  # 나누기
        result += 1     # 카운트
    else:
        result += n % k # n이 k에 나누어 떨어질 때까지 한번에 카운트
        n -= (n % k)    #한번에 빼기
print(result)