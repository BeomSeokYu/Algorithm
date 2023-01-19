'''
병합 정렬 : 퀵 정렬과 같은 분할 정복 알고리즘을 사용하는 정렬 알고리즘.
            일단 반으로 나누고 나중에 정렬하는 방식
 - 퀵 정렬과 다르게 피벗 값에 상관없이 정확히 반을 나누어 정렬하므로 최악의 경우에도 O(N * logN)의 시간 복잡도를 보장한다.
 [방법]
 - 다 쪼개진 원소들을 합치면서 정렬을 수행
 - 합쳐진 배열은 정렬이 됨
 - 최종적으로 합쳐지면 정렬이된 전체 배열을 얻음
시간 복잡도 : O(N * logN)
'''
# 스왑 메소드
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
# 재귀를 이용하여 퀵 정렬 수행
def mergeSort(start, end):
    if end == start:
        return start
    else:
        half = (end - start) // 2
        l = mergeSort(start, half)
        r = mergeSort(half+1, end)
    
        

# 정렬할 리스트 입력
list = list(map(int, input("병합 정렬할 숫자를 띄어쓰기로 구분하여 입력 : ").split(' ')))
n = len(list)
# 병합 정렬
print()
mergeSort(list)
# 정렬된 리스트 출력
for i in list:
    print(i, end=' ')