'''
/*********************************************************************
*Title : 단어 수학
*Number : null
*Author : <img src="https://static.solved.ac/tier_small/11.svg" class="solvedac-tier"> ro1864
*Description : 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오. 
*Input : 첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다. 
*Output : 첫째 줄에 주어진 단어의 합의 최댓값을 출력한다. 
*Start Time : 2023년 1월 6일 14시 6분 47초
*End Time : 2023년 1월 6일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/

CSDAEWR
ASDQWER
SDAWSCA
AQQWSXZ
'''


import sys
input = sys.stdin.readline

wordList = []
_maxLen = 0

# 단어들 입력받아 단어 길이 최댓값 _maxLen과 wordList를 만듬
n = int(input()) # 1 < n <= 10
for i in range(n):
    temp = list(input().rstrip())
    size = len(temp)
    if size > _maxLen:
        _maxLen = size
    wordList.append(temp)

scores = {}     # 각 단어들의 문자별 점수를 담을 딕셔너리
while True:
    for word in wordList:
        if len(word) > _maxLen - 1:
            char = word[len(word) - _maxLen]    # 가장 자릿수가 높은 문자들부터 선택
            if char not in scores:          # scores에 없으면 추가
                scores[char] = 0
            scores[char] += 10 ** _maxLen   # 각 자릿수에 맞는 점수 부여

    _maxLen -= 1
    if _maxLen == 0:    # 1의 자릿수 까지 확인했으면 끝
        break

# 점수별로 정렬한 (문자:점수) 리스트 만들기
sortedScores = sorted(scores.items(), key=lambda x : x[1], reverse=True)

# 각 문자별 숫자 할당
num = 9
for i in sortedScores:
    scores[i[0]] = num
    num -= 1

# 문자들을 숫자화하여 결과 출력
result = []
for word in wordList:
    numberStr = ''
    for char in word:
        numberStr += str(scores[char])
    result.append(int(numberStr))
print(sum(result))