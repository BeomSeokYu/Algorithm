#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2024/11/21 12:48:18 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())

T_result = 0
for m in size_list:
  if m == 0:
    continue
  else:
    T_result += m // T
    if m % T != 0:
      T_result += 1
print(T_result)

print('%d %d' % (N//P, N%P))