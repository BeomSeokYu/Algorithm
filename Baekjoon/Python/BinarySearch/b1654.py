import sys
input = sys.stdin.readline

def paramSearch(arr, t, s, e):
    result = 0                      # 최적화 값 담을 변수
    while s <= e:
        m = (s + e) // 2
        cnt = 0                     # 자른 랜선의 수 담을 변수
        for i in arr:               # 모든 랜선을
            cnt += i // m           # 설정한 절반 길이로 잘라 나온 갯수 더함
        if cnt >= t:                # 타겟 수보다 같거나 크면
            result = m              # 결괏값에 저장하고
            s = m + 1               # 더 길게 자를 수 있는지 확인을 위해 시작길이 올림
        else:                       # 타겟 수보다 작으면
            e = m - 1               # 더 잘게 자르기
    return result                   # 최적의 결과 반환

k, n = map(int, input().split())
li = []
for i in range(k):
    li.append(int(input()))
print(paramSearch(li, n, 1, max(li)))
# 0으로 나누는 문제(ZeroDivisionError) 발생으로 1부터
# 가장 긴 랜선의 길이 까지