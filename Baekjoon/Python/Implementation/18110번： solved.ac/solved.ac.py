#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18110                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18110                          #+#        #+#      #+#     #
#    Solved: 2024/11/24 16:40:27 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def round(d):
  if d + 0.5 >= int(d) + 1:
    return int(d) + 1
  elif d + 0.5 < int(d) + 1:
    return int(d)
  return 0

n = int(input())
avg = 0
if n > 0:
  li = []
  for i in range(n):
    li.append(int(input()))
  li.sort()

  per_15 = round(((n / 100) * 15))
  for i in range(per_15, n - per_15):
    avg += li[i]

  avg = round(avg / (n - (per_15 * 2)))
print(avg)