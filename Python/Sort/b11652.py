import sys
input = sys.stdin.readline

resDic = {}
for i in range(int(input())):
    num = int(input())
    if num not in resDic:
        resDic[num] = 1
    else:
        resDic[num] += 1
result = sorted(resDic.items(), key=lambda x:x[1])
print(result)
