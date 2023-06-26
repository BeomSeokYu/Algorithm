import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in list(str(h)+str(m)+str(s)):
                cnt += 1
print(cnt)