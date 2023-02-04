'''
/*********************************************************************
*Title : A → B
*Number : null
*Author : <img src="https://static.solved.ac/tier_small/11.svg" class="solvedac-tier"> ro1864
*Description : 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.2를 곱한다.1을 수의 가장 오른쪽에 추가한다. A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자. 
*Input : 첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다. 
*Output : A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다. 
*Start Time : 2023년 1월 4일 23시 41분 20초
*End Time : 2023년 1월 4일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/


'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1
while b != a and b != 0:
    if str(b)[-1] == '1':
        b = int((b - 1) / 10)
    elif b % 2 == 0:
        b = int(b / 2)
    else:
        cnt = -1
        break
    cnt += 1
print(cnt) if b != 0 else print(-1)