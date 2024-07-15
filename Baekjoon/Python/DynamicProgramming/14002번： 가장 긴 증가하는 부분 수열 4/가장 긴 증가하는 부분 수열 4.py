#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14002                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14002                          #+#        #+#      #+#     #
#    Solved: 2024/06/19 13:17:11 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def lis(p, n):
    dp = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] < p[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    return dp

def findSequence(dp, a):
    subsequence = []
    order = max(dp)
    for i in range(n - 1, -1, -1):
        if dp[i] == order:
            subsequence.append(a[i])
            order -= 1
    subsequence.reverse()
    return subsequence

n = int(input())
a = list(map(int, input().split()))

dp = lis(a, n)

print(max(dp))
print(*findSequence(dp, a), sep=' ')