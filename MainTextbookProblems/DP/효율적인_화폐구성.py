import sys
input = sys.stdin.readline

'''
ai = 금액i를 만들 수 있는 최소한의 화폐 개수
k = 화폐의 단위
ai-k = (i - k)를 만들 수 있는 최소한의 화폐 개수

- ai-k를 만드는 방법이 존재하는 경우 : ai = min(ai, ai-k + 1)
- ai-k를 만드는 방법이 존재하지 않는 경우 : ai = 10001
'''

n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

d = [10001] * (m + 1)
d[0] = 0

for k in coins:
    for i in range(k, m + 1):
        d[i] = min(d[i], d[i - k] + 1)
print(d[m]) if d[m] < 10001 else print(-1)