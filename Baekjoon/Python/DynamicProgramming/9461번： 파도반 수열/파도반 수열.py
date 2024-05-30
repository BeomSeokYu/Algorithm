#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9461                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9461                           #+#        #+#      #+#     #
#    Solved: 2024/05/30 11:24:51 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
[파도반 수열]
1 1 1 2 2 3 4 5 7 9 12 16 21 ...
=> n = n - 2 + n - 3
'''

import sys
input = sys.stdin.readline

def pado(n):
    dp = [0] * (n + 1) # table
    dp[1] = 1
    if n > 1:
        dp[2] = 1
    if n > 2:
        dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(pado(n))