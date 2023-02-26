import sys
input = sys.stdin.readline

cntDic = {}                 # {숫자 : 갯수} 딕셔너리
n = int(input())
for i in range(n):
    num = int(input())
    if num not in cntDic:   # 아직 키가 아니면
        cntDic[num] = 1     # 1
    else:                   # 이미 키가 있으면
        cntDic[num] += 1    # +1
result = sorted(cntDic.items(), key=lambda x: x[0])         # 먼저 키로 정렬
result = sorted(result, key=lambda x: x[1], reverse=True)   # 값 내림차순으로 정렬
print(result[0][0])                                         # 가장 앞의 값 출력
