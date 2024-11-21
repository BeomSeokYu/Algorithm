#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15829                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15829                          #+#        #+#      #+#     #
#    Solved: 2024/11/21 13:05:04 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

r = 31
M = 1234567891

L = int(input())
s = input().rstrip()
hash = 0
for i in range(0, L):
  a = ord(s[i]) - 96
  ar = a * (r ** i)
  hash += ar

hash = (hash) % M

print(hash)