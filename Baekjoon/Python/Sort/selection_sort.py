'''
선택 정렬 : 가장 작은 것을 선택해서 제일 앞으로 보내는 알고리즘
 - 가장 윈시적이고 기초적인 방법이며 비효율적임
시간 복잡도 : O(N^2)
'''
# 스왑 메소드
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
# 정렬할 리스트 입력
list = list(map(int, input("선택 정렬할 숫자를 띄어쓰기로 구분하여 입력 : ").split(' ')))
n = len(list)
# 선택 정렬
index = 0
for i in range(0, n):
    min = 9999
    for j in range(i, n):
        if min > list[j]:
            min = list[j]
            index = j
    list[i], list[index] = swap(list[i], list[index])
# 정렬된 리스트 출력
for i in list:
    print(i, end=' ')