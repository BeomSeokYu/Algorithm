'''
/*********************************************************************
*Title : 뒤집기
*Number : null
*Author : <img src="https://static.solved.ac/tier_small/11.svg" class="solvedac-tier"> ro1864
*Description : 다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다. 다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.예를 들어 S=0001100 일 때,전체를 뒤집으면 1110011이 된다.4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오. 
*Input : 첫째 줄에 문자열 S가 주어진다. S의 길이는 100만보다 작다. 
*Output : 첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다. 
*Start Time : 2023년 1월 4일 23시 21분 45초
*End Time : 2023년 1월 4일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/


'''

import sys
input = sys.stdin.readline

s = input().rstrip()
preNum = int(s[0])
group = [0, 0]
group[preNum] += 1
for i in s:
    if int(i) != preNum:
        group[int(i)] += 1
        preNum = int(i)
print(min(group[0], group[1]))