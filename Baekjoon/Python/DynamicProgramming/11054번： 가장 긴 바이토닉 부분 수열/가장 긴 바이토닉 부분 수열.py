#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11054                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11054                          #+#        #+#      #+#     #
#    Solved: 2024/06/13 14:34:10 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
[바이토닉 수열]
수열 S가 어떤 수 S_k를 기준으로 S_1 < S_2 < ... S_(k-1) < S_k > S_(k+1) > ... S_(N-1) > S_N을 만족하는 수열

문제
- 수열이 주어졌을 때, 그 수열에서 가장 긴 바이토닉 부분 수열을 구하면 됨
-> 어려운 DP...
-> LIS(최장 증가 부분 수열) 응용 문제

'''
import sys
input = sys.stdin.readline

def lis(p, n):
    rev_p = p[::-1]
    leng = [1] * n
    rev_leng = [1] * n
    total_leng = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] < p[j]:
                leng[j] = max(leng[j], leng[i] + 1)
            if rev_p[i] < rev_p[j]:
                rev_leng[j] = max(rev_leng[j], rev_leng[i] + 1)
    for i in range(n):
        total_leng[i] = leng[i] + rev_leng[n - i - 1]
    return max(total_leng) - 1

n = int(input())
p = list(map(int, input().split()))

print(lis(p, n))