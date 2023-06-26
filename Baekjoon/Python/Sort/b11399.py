import sys
input = sys.stdin.readline

n = int(input())
list = sorted(list(map(int, input().split())))

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += list[j]
print(sum)