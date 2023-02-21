'''
/*********************************************************************
*Title : N과 M (1)
*Number : null
*Author : <img src="https://static.solved.ac/tier_small/10.svg" class="solvedac-tier"> ro1864
*Description :  자연수 N과 M이 주어졌을 때,
                아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
                1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
*Input : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
*Output : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.수열은 사전 순으로 증가하는 순서로 출력해야 한다. 
*Start Time : 2023년 1월 1일 10시 0분 40초
*End Time : 2023년 1월 1일 시 분 초
*comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
*********************************************************************/
5 3
[1 2 3 4 5]

1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 1 3
2 1 4
2 1 5
2 3 4
2 3 5
2 4 5

5 4
[1 2 3 4 5]

1 2 3 4
1 2 3 5
1 2 4 3
1 2 4 5
1 2 5 3
1 2 5 4
1 3 2 4
1 3 2 5
1 3 4 5
...

7 3
[1, 2, 3, 4, 5, 6, 7]
123
124
125
126
127
131
132
134
135
136
137
141
142
143
'''
import sys
input = sys.stdin.readline

# n, m = map(int, input().split())
# for li in itertools.permutations(range(1, n + 1), m):
#     for i in li:
#         print(i, end= ' ')
#     print()

def permutation(li, m):
    idx = m
    result = []
    fix = [li[i] for i in range(m)]
    for i in range(len(fix)):
        temp = [i for i in fix]
        for j in range(len(li)):
            if j not in fix:
                temp.append(li[j])
        result.append(temp)
        idx = m - 1