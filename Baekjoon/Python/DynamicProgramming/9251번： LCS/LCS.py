#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2024/06/17 13:30:55 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
LCS(Longest Common Subsequence, 최장 공통 부분 수열)

=> LIS를 응용


점화식:
- 만약 X[i-1]와 Y[j-1]가 같다면, dp[i][j] = dp[i-1][j-1] + 1
- 다르다면, dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        0   1   2   3   4   5   6
            A   C   A   Y   K   P
0       0   0   0   0   0   0   0
1   C   0   0   1   1   1   1   1
2   A   0   1   1   2   2   2   2
3   P   0   1   1   2   2   2   3
4   C   0   1   2   2   2   2   3
5   A   0   1   2   3   3   3   3
6   K   0   1   2   3   3   4   4

'''
import sys
input = sys.stdin.readline

def lcs(p1, p2):
    leng = [[0 for _ in range(len(p2) + 1)] for _ in range(len(p1) + 1)]
    _max = 0
    for i in range(1, len(p1) + 1):
        for j in range(1, len(p2) + 1):
            if p1[i-1] == p2[j-1]:
                leng[i][j] = leng[i-1][j-1] + 1
            else:
                leng[i][j] = max(leng[i-1][j], leng[i][j-1])
            if _max < leng[i][j]:
                _max = leng[i][j]
    return _max
a = list(input().rstrip())
b = list(input().rstrip())
print(lcs(a, b))