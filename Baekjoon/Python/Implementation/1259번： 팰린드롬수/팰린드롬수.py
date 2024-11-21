#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1259                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1259                           #+#        #+#      #+#     #
#    Solved: 2024/11/21 12:40:36 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

while True:
  str = input().rstrip()
  if (str == '0'):
    break
  s = 0
  e = len(str) - 1
  result = 'yes'
  while s < e:
    if str[s] != str[e]:
      result = 'no'
      break
    s += 1
    e -= 1

  print(result)