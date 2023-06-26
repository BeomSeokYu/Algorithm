'''
버블 정렬 : 옆에 있는 값과 비교하여 더 작은 값을 반복적으로 앞으로 보내는 알고리즘
            (앞에서 부터 큰 값을 뒤로 보내는 것과 같음)
 - 구현이 가장 쉽지만 가장 비효율적인 알고리즘 : 매번 스왑을 해야하기 때문
시간 복잡도 : O(N^2)
'''

# 스왑 메소드
def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
# 정렬할 리스트 입력
list = list(map(int, input("버블 정렬할 숫자를 띄어쓰기로 구분하여 입력 : ").split(' ')))
n = len(list)
# 버블 정렬
for i in range(0, n):
    for j in range(1, n-i):
        if list[j-1] > list[j]:
            list[j - 1], list[j] = swap(list[j-1], list[j])
# 정렬된 리스트 출력
for i in list:
    print(i, end=' ')