import sys
input = sys.stdin.readline

pay = int(input())
ret = 1000 - pay
result = 0
coin = [500, 100, 50, 10, 5, 1]
for i in coin:
    result += ret // i
    ret %= i
print(result)