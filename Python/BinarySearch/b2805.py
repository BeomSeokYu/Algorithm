import sys
input = sys.stdin.readline

# 이진 탐색 함수
def bSearch(arr, t, s, e):
    result = 0                  # 최적화 되는 나무 길이값을 저장할 변수
    while s <= e:               # s > e가 아니면 계속 반복
        h = (s + e) // 2        # 중간 길이
        t_len = 0               # 자른 나무들의 길이 합을 저장할 변수
        for i in arr:           # 모든 나무들을 반복하며
            if i > h:           # 기준 길이 보다 크면
                t_len += i - h  # 잘라진 값을 합함
        if t_len > t:           # 그 합이 타겟보다 크면
            result = h          # 조건을 만족하므로 결괏값에 저장
            s = h + 1           # 덜 잘라봐야 하므로 높이를 절반 높이기 위해 조정
        elif t_len < t:         # 타겟 보다 작으면
            e = h - 1           # 더 잘라야 하므로 높이를 절반 낮추기 위해 조정
        else:
            return h            # 타겟과 일치하면 바로 반환 (최적화된 길이)
    return result               # 반복문이 종료되면 result에 남아 있는 값이 최적화 값

n, m = map(int, input().split())                # 나무 수, 타겟 길이 입력
th = sorted(list(map(int, input().split())))    # 나무 길이 리스트 입력
print(bSearch(th, m, 0, th[-1]))                # 이진 탐색 결과 (절단기 최적화 높이 값) 출력