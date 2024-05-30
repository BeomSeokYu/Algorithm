#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1149                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1149                           #+#        #+#      #+#     #
#    Solved: 2024/05/30 13:47:46 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
[조건]
1.  (n)_color != (n-1)_color

2.  i(2 ≤ i ≤ n-1)_color != (i-1)
    i(2 ≤ i ≤ n-1)_color != (i+1)

(n)_color[0] = min((n-1)[0] + (n-1)[1], (n-1)[0] + (n-1)[2])
(n)_color[1] = min((n-1)[1] + (n-1)[0], (n-1)[1] + (n-1)[2])
(n)_color[2] = min((n-1)[2] + (n-1)[0], (n-1)[2] + (n-1)[1])
'''
import sys
input = sys.stdin.readline

n = int(input())

dp = []

for i in range(n):
    r, g, b = map(int, input().split())
    if i == 0:
        dp = [r, g, b]
        continue
    r1 = min(r + dp[1], r + dp[2])
    g1 = min(g + dp[0], g + dp[2])
    b1 = min(b + dp[0], b + dp[1])
    dp = [r1, g1, b1]

print(min(dp))