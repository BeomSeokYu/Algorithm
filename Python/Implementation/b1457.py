import sys, math
input = sys.stdin.readline

n = list(map(int, list(input().rstrip())))
result = [0] * 9                         # 필요한 수 갯수 카운트 할거임
for i in n:
    result[6 if i in (6, 9) else i] += 1 # 6, 9 는 6으로 카운트 할거임
result[6] = math.ceil(result[6]/2)       # 2로 나누고 올림 할거임
print(max(result))                       # 제일 큰거 만큼 세트 살거임