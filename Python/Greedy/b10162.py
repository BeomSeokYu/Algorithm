import sys
input = sys.stdin.readline

btn = [300, 60, 10]

t = int(input())

for i in btn:
    if t % 10 != 0:
        print(-1)
        break
    cnt = 0
    cnt = t // i
    t %= i
    print(cnt, end=' ')