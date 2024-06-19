#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12015                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12015                          #+#        #+#      #+#     #
#    Solved: 2024/06/19 10:11:47 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def lis(p):
    dp = []
    for i in p:
        idx = binary_search(dp, i, 0, len(dp) - 1)

        if idx == len(dp):
            dp.append(i)
        else:
            dp[idx] = i
    return len(dp)

n = int(input())
a = list(map(int, input().split()))

print(lis(a))