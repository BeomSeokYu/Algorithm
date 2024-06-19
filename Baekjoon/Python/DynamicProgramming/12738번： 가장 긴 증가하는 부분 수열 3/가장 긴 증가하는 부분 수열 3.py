#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12738                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12738                          #+#        #+#      #+#     #
#    Solved: 2024/06/19 12:49:23 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start # target이 없을 경우

def lis(p):
    dp = []
    for i in p:
        idx = binary_search(dp, i)
        if idx == len(dp):
            dp.append(i)
        else:
            dp[idx] = i
    return len(dp)

n = int(input())
a = list(map(int, input().split()))
print(lis(a))