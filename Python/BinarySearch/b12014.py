import sys
input = sys.stdin.readline

'''
Longest Increasing Sequence(LIS; 최장 증가 부분 수열)의 개념을 알아야 함
 - 수열 중 증가하는 부분만을 뽑았을 때 그 길이가 가장 긴 수열

DP만 사용하면 O(N^2)의 시간 복잡도,
이진 탐색을 사용하면 O(NLogN)의 시간 복잡도 가능
'''

'''
DP 풀이.. 시간초과 떠버림..
'''
# for i in range(int(input())):
#     n, k = map(int, input().split())

#     d = [1] * (n + 1)
#     arr = list(map(int, input().split()))
#     for i in range(n):
#         for j in range(i):                                  # 이전 부분을 전부 다시 탐색해야 한다? -> 이진 탐색을 쓴다면 좋을것?
#             if arr[i] > arr[j]:
#                 d[i] = max(d[i], d[j] + 1)
#     _max = max(d)
#     print('Case #%d\n%d'%((i+1), 1 if _max == k else 0))

'''
이분 탐색 방법
'''
def bSearch(d, t, s, e):
    result = 0
    while s <= e:
        m = (s + e) // 2
        if d[m] == t:
            return m     # 타겟과 같으면 인덱스 반환
        elif d[m] > t:   # 타겟이 해당 값보다 작고 해당 값과 같을수록 최적해
            result = m
            e = m - 1
        else:
            s = m + 1
    return result        # 최적의 인덱스 반환

for c in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    lis = [arr[0]]                # 첫번째 값 담음
    for i in range(1, n):
        if arr[i] > lis[-1]:      # arr[i]가 d의 마지막 값보다 크면
            lis.append(arr[i])    # 넣음 (d는 오름차순 정렬되는 리스트)
        else:                     # 작거나 같으면
            idx = bSearch(lis, arr[i], 0, len(lis) - 1) # d에서 arr[i]보다 작고 가장 가까운 값의 인덱스를 찾아옴
            lis[idx] = arr[i]     # 그 인덱스에 값 넣음
    # 형식에 맞게 출력
    print('Case #%d\n%d'%((c+1), 1 if len(lis) >= k else 0)) # LIS가 k보다 길거나 같으면 조건에 만족