import sys
input = sys.stdin.readline

cntDic = {}
n = int(input())
for i in range(n):
    num = int(input())
    if num not in cntDic:
        cntDic[num] = 1
    else:
        cntDic[num] += 1
result = sorted(cntDic.items(), key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1], reverse=True)
print(result[0][0])