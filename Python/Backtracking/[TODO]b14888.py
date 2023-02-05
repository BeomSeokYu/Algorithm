'''
문제
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다.
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다.
이때, 주어진 수의 순서를 바꾸면 안 된다.
예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고,
주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는
총 60가지의 식을 만들 수 있다.
예를 들어, 아래와 같은 식을 만들 수 있다.
1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
또, 나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때는 C++14의 기준을 따른다.
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때,
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

예제 입력 1  복사
2
5 6
0 0 1 0
예제 출력 1  복사
30
30
예제 입력 2  복사
3
3 4 5
1 0 1 0
예제 출력 2  복사
35
17
예제 입력 3  복사
6
1 2 3 4 5 6
2 1 1 1
예제 출력 3  복사
54
-24
힌트
세 번째 예제의 경우에 다음과 같은 식이 최댓값/최솟값이 나온다.

최댓값: 1-2÷3+4+5×6
최솟값: 1+2+3÷4-5×6
'''

'''
자 풀어보자
[최댓값 규칙]
[- / + *] 가 맞을까?
1 2 3 4 5 6
 - - / + *
-1 -3 -1 4 24
[+ / - *] 가 맞을까?
3 1 -3 -8 -48
모든 연산이 있는게 아니라도 위의 규칙이 맞을까?
1 2 3 4 5 6
 - - / + +
-1 -4 -1 4 10
3 6 1 -4 -10
- 가 없는 경우는?
[/ + *]
[* + /]
'''
import sys, math
input = sys.stdin.readline

#입력
n = int(input())
aList = list(map(int, input().split()))     # 숫자 리스트
aList.sort()
operNum = list(map(int, input().split()))   # 연산자 갯수 리스트
oper = ['+', '-', '*', '/']                 # 각 인덱스 별 연산자
maxRaw = [1, 3, 0, 2]                       # 마이너스를 포함해 최댓값을 갖는 경우 연산자 순서
minRaw = [0, 3, 1, 2]                       # 마이너스를 포함해 최솟값을 갖는 경우 연산자 순서
maxRawNo = [3, 0, 2]                        # 마이너스 없이 최댓값을 갖는 경우 연산자 순서
minRawNo = [2, 0, 3]                        # 마이너스 없이 최솟값을 갖는 경우 연산자 순서

def makeExp(aList, operNum, rawList):
    temp = aList[:]                         # 숫자 리스트 클론
    insertIdx = 1
    for j in rawList:
        for k in range(operNum[j]):
            temp.insert(insertIdx, oper[j])
            insertIdx += 2
    return temp

def calExp(expList):
    result = expList[0]
    for j in range(1, len(expList), 2):
        result = int(eval(str(result) + expList[j] + str(expList[j + 1])))
    return result

def getMinMaxList():
    maxExpList = []
    minExpList = []
    if operNum[1] > 0:
        maxExpList = makeExp(aList, operNum, maxRaw)
        minExpList = makeExp(aList, operNum, minRaw)
    else:
        minExpList = makeExp(aList, operNum, minRawNo)
        maxExpList = makeExp(aList, operNum, maxRawNo)
    return minExpList, maxExpList

minEL, maxEL = getMinMaxList()

print(calExp(maxEL))
print(calExp(minEL))