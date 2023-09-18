import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
for i in range(5):
    li[i] = li[i] ** 2
print(sum(li)%10)