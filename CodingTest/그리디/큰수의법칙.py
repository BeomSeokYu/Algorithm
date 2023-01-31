import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
# 입력받은 수를 내림차순 정렬한 리스트 생성
li = sorted(list(map(int, input().split())), reverse=True)
# 규칙적으로 반복되는 횟수만큼 곱해주고, 나머지는 가장 큰 수의 횟수로 계산
print((li[0] * k + li[1]) * (m // (k + 1)) + (li[0] * (m % (k + 1))))