'''
퀵 정렬 : 대표적인 '분할 정복' 알고리즘(Divide and conquer algorithm)으로, 
특정한 값을 기준으로 큰 숫자와 작은 숫자를 서로 교환한 뒤에 배열을 반으로 나누는 것을 반복 하는 알고리즘.
 [규칙]
 - 기준 값인 피벗(Pivot)이 필요 (보통 첫 번째 원소를 피벗으로 사용함)
 - 기준 값보다 큰 값을 배열의 왼쪽부터, 작은 값을 오른쪽부터 찾음.
 - 작은 값의 인덱스가 큰 값의 인덱스보다 크면, 작은 값과 큰 값을 교환.
 - 작은 값의 인덱스가 큰 값의 인덱스보다 작으면, 피벗 값과 작은 값을 교환.
 - 위 과정을 기준 값의 좌우측에 반복
시간 복잡도:    O(N * logN)   (평균)
               O(N^2)        (최악)         -> 피벗값에 따라 최악의 경우가 생길 수 있음 [ex) 이미 정렬된 배열]
'''
# 스왑 메소드
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
# 재귀를 이용하여 퀵 정렬 수행
def quickSort(start, end):
    if start>=end:  # 원소가 1개인 경우 그대로 둠
        return
    pivot = start   # 피벗은 첫번째 원소
    i = start + 1
    j = end
    while i <= j:   # 엇갈릴 때까지 반복
        while(i <= end and list[i] <= list[pivot]):     #끝에 도달하거나 피벗보다 큰 값을 찾을 때까지 반복
            i = i + 1
        while(j > start and list[j] >= list[pivot]):    #피벗에 도달하거나 피벗보다 작은 값을 찾을 때까지 반복
            j = j - 1
        if(i > j):  # 엇갈린 상태(작은 값의 인덱스가 큰 값의 인덱스보다 작으면, 피벗 값과 작은 값을 교환)
            list[pivot], list[j] = swap(list[pivot], list[j])
        else:       # 엇갈리지 않은 상태 (작은 값의 인덱스가 큰 값의 인덱스보다 크면, 작은 값과 큰 값을 교환)
            list[i], list[j] = swap(list[i], list[j])
    quickSort(start, j - 1); # 피벗보다 작은 값들에 대해서도 새로운 피벗을 설정하여 퀵정렬 실행
    quickSort(j + 1, end);     # 피벗보다 큰 값들에 대해서도 새로운 피벗을 설정하여 퀵정렬 실행
# 정렬할 리스트 입력
list = list(map(int, input("퀵 정렬할 숫자를 띄어쓰기로 구분하여 입력 : ").split(' ')))
n = len(list)
# 퀵 정렬
quickSort(0, n-1)
# 정렬된 리스트 출력
for i in list:
    print(i, end=' ')