#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2565                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2565                           #+#        #+#      #+#     #
#    Solved: 2024/06/14 15:49:53 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''

'''
import sys
input = sys.stdin.readline

def lis(p, n):
    length = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if p[i][1] < p[j][1]:
                length[j] = max(length[j], length[i] + 1)
    return max(length)

n = int(input())
p = []
for i in range(n):
    p.append(tuple(map(int, input().split())))
p.sort(key = lambda x:x[0])
max_len = lis(p, n)
print(n - max_len)