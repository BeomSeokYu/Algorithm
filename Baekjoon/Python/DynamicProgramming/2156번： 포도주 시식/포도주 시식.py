#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2156                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2156                           #+#        #+#      #+#     #
#    Solved: 2024/05/31 09:14:12 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
조건
- 3잔을 연속해서 마실 수는 없다 -> 연속해서 2잔까지
- 위의 조건에서 가장 많이 마실 수 있는 경우를 찾아야 함
-> DP 사용
'''
import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * n

li = []
for _ in range(n):
    li.append(int(input()))

for i in range(n):
    if i == 0:
        dp[i] = li[i]
    elif i == 1:
        dp[i] = li[i] + li[i-1]
    elif i == 2:
        dp[i] = max(dp[i-1], dp[i-2] + li[i], li[i-1] + li[i])
    else:
        dp[i] = max(dp[i-1], dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i])

print(max(dp))