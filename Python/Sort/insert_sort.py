'''
삽입 정렬 : 각 숫자를 적절한 위치에 삽입하는 알고리즘
            (뒤로 가면서 앞의 숫자 크기를 보고 그 사이에 적절히 삽입)
 - 선택, 버블 정렬에 비해 필요한 경우에만 위치를 바꿔 좀 더 효율적임
 - 미리 어느정도 정렬이 되어 있다면 아주 빠르게 끝낼 수 있음
시간 복잡도 : O(N^2) (최악의 경우)
'''

# 스왑 메소드
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
# 정렬할 리스트 입력
list = list(map(int, input("삽입 정렬할 숫자를 띄어쓰기로 구분하여 입력 : ").split(' ')))
n = len(list)
# 삽입 정렬
    # while 문
for i in range(1, n):
    key = list[i] # key : 정렬할 원소
    j = i - 1
    while j >= 0 and list[j] > key:
        list[j+1] = list[j]
        j = j - 1
    list[j+1] = key
    # for 문
'''for i in range(0, n-1):
    #for j in range(0, i+1):
    #    print(list[j], end=' ')
    for j in range(0, i+1):
        if list[i-j] > list[i-j + 1]:
            list[i-j], list[i-j + 1] = swap(list[i-j], list[i-j + 1])
    #print("")'''
# 정렬된 리스트 출력
for i in list:
    print(i, end=' ')