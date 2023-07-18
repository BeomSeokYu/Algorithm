import sys
input = sys.stdin.readline

words = {}

N, M = map(int, input().split())
for _ in range(N):
    str = input().rstrip()
    if len(str) < M:
        continue
    try:
        words[str] += 1
    except KeyError:
        words[str] = 1
result = list(words.items())
result.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in result:
    print(i[0])