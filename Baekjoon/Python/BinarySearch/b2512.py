import sys
input = sys.stdin.readline

def bSearch(arr, t, s, e):
    result = 0                              # 최적화 값 저장할 변수
    while s <= e:
        mid = (s + e) // 2                  # 시작 끝 액수의 중간값
        pSum = 0                            # 총액 넣을 변수
        for i in arr:
            pSum += mid if i > mid else i   # 예산에 따른 총액 계산
        if pSum > t:                        # 예산보다 크면
            e = mid - 1                     # 줄여서 반
        elif pSum < t:                      # 예산보다 작으면
            result = mid                    # 일단 해로 넣고
            s = mid + 1                     # 더 큰 반
        else:
            return mid                      # 상한값이면 바로 리턴
    return result                           # 최적화 값 리턴

n = int(input())
li = list(map(int, input().split()))
t = int(input())
print(bSearch(li, t, 0, max(li)))