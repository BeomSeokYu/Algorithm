import sys, time
input = sys.stdin.readline

def selection(n, list):
    for i in range(n-1):
        _min = list[i]                              # 가장 작은 값으로 처음 값 선택
        idx = i                                     # 처음 값 인덱스
        for j in range(i+1, n):
            if list[j] < _min:                      # 다음 값들은 다 돌며 가장 작은 값 선택
                _min = list[j]
                idx = j
        list[i], list[idx] = list[idx], list[i]     # 정렬되지 않은 가장 앞의 값과 선택된 가장 작은 값을 스왑
    return list

def bubble(n, list):
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:                     # 다음값과 비교해 더 크면
                list[j], list[j+1] = list[j+1], list[j] # 바꿔서 끝에부터 정렬
    return list

def insertion(n, list):
    for i in range(1, n):
        key = list[i]                       # key : 정렬할 원소
        idx = i - 1
        while idx >= 0 and list[idx] > key:
            list[idx+1] = list[idx]         # 정렬할 값보다 크면 한칸씩 미룸
            idx -= 1
        list[idx+1] = key                   # 작은거 뒤에 키를 넣음
    return list

def quick(n, list, start, end):
    if start >= end:            # 원소가 1개인 경우 그대로 둠
        return
    pivot = start               # 피벗은 첫번째 원소
    i = start + 1
    j = end
    while i <= j:               # 엇갈릴 때까지 반복
        while(i <= end and list[i] <= list[pivot]):     #끝에 도달하거나 피벗보다 큰 값을 찾을 때까지 반복
            i = i + 1
        while(j > start and list[j] >= list[pivot]):    #피벗에 도달하거나 피벗보다 작은 값을 찾을 때까지 반복
            j = j - 1
        if(i > j):                                      # 엇갈린 상태(작은 값의 인덱스가 큰 값의 인덱스보다 작으면, 피벗 값과 작은 값을 교환)
            list[pivot], list[j] = list[j], list[pivot]
        else:                                           # 엇갈리지 않은 상태 (작은 값의 인덱스가 큰 값의 인덱스보다 크면, 작은 값과 큰 값을 교환)
            list[i], list[j] = list[j], list[i]
    quick(n, list, start, j - 1);                                # 피벗보다 작은 값들에 대해서도 새로운 피벗을 설정하여 퀵정렬 실행
    quick(n, list, j + 1, end);                                  # 피벗보다 큰 값들에 대해서도 새로운 피벗을 설정하여 퀵정렬 실행
    return list

def merge(n, list):
    if len(list) < 2:                                   # 1개면 그냥 리턴
        return list

    mid = len(list) // 2                                # 중간값
    lList = merge(n, list[:mid])                        # 왼쪽 리스트 재귀 호출
    rList = merge(n, list[mid:])                        # 오른쪽 리스트 재귀 호출

    mergedList = []
    l = r = 0
    while l < len(lList) and r < len(rList):            # (정렬된) 두 리스트 비교해서 정렬
        if lList[l] < rList[r]: # l is  greater
            mergedList.append(lList[l])
            l += 1
        else:
            mergedList.append(rList[r])
            r += 1
    mergedList += lList[l:]                             # 나머지 이어붙임
    mergedList += rList[r:]
    return mergedList                                   # 정렬된 리스트 정렬

n = int(input())
li = list(map(int, input().split()))

timeList = []

print(*selection(n, li), sep=" ")
print(*bubble(n, li), sep=" ")
print(*insertion(n, li), sep=" ")
print(*quick(n, li, 0, n-1), sep=" ")
print(*merge(n, li), sep=" ")