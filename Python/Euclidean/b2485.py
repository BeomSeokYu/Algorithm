import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li.sort()

step = []
for i in range(len(li)-1):
    step.append(li[i+1] - li[i])
step.sort()

gcdNum = 0
for i in range(len(step)):
    gcdNum = gcd(max(step[i], gcdNum), min(step[i], gcdNum))

cnt = 0
for i in step:
    cnt += (i // gcdNum) - 1

print(cnt)