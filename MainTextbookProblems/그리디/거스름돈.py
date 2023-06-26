import sys
input = sys.stdin.readline

result = 0
# 큰 코인 순으로 정렬된 상태여야 함
coins = [500, 100, 50, 10]
n = int(input())
for coin in coins:
    result += n // coin # 큰 액수부터 거스름돈 갯수 저장
    n %= coin           # 나머지 금액 저장
print(result)