import sys
input = sys.stdin.readline

coinList = []
cnt = 0

n, k = map(int, input().split())

for _ in range(n):
    coinList.append(int(input()))
coinList.sort(reverse=True)

for coin in coinList:
    cnt += k // coin
    k %= coin
print(cnt)