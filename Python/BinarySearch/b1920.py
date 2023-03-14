import sys
input = sys.stdin.readline

# 이진 탐색 함수
def bSearch(arr, t, s, e):
    while s <= e:               # 교차할때까지 반복
        mid = (s + e) // 2      # 인덱스 중간값
        if arr[mid] == t:       # 리스트 중간이 타겟이면
            return 1            # 1 리턴
        elif arr[mid] > t:      # 터겟보다 크면
            e = mid - 1         # 끝 인덱스 값 조정
        elif arr[mid] < t:      # 타겟보다 작으면
            s = mid + 1         # 시작 인덱스 값 조정
    return 0                    # 탐색이 끝났으면 없는 것

# 입력 받기
n = int(input())
li = sorted(list(map(int, input().split())))    # 오름차순 정렬
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(bSearch(li, t, 0, n-1))   # 타겟들을 이진 탐색으로 탐색