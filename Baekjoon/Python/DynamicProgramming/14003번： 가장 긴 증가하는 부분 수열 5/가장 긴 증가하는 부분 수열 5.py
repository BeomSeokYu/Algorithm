#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14003                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14003                          #+#        #+#      #+#     #
#    Solved: 2024/07/15 10:49:11 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

def b_search(target, arr):
  s = 0
  e = len(arr) - 1
  while s <= e:
    mid = (s + e) // 2
    if target == arr[mid]:
      return mid
    elif target < arr[mid]:
      e = mid - 1
    else:
      s = mid + 1
  return s

def lis(a):
  dp = [(0, a[0])]  # 모든 기록
  li = [a[0]]
  for i in range(1, len(a)):
    if a[i] > li[-1]:
      li.append(a[i])
      dp.append((len(li) - 1, a[i]))
    else:
      idx = b_search(a[i], li)
      li[idx] = a[i]
      dp.append((idx, a[i]))
  return dp, li

def backtracking(li, dp):
  s = []
  order = len(li) - 1
  for i in range(len(dp) - 1, -1, -1):
    if dp[i][0] == order:
      s.append(dp[i][1])
      order -= 1
  s.reverse()
  return s


n = int(input())
a = list(map(int, input().split()))

dp, li = lis(a)
print(len(li))
print(*backtracking(li, dp))