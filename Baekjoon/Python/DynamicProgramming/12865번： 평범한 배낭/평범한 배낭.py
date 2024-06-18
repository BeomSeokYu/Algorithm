#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12865                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12865                          #+#        #+#      #+#     #
#    Solved: 2024/06/18 10:26:56 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [(0, 0)]
for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])