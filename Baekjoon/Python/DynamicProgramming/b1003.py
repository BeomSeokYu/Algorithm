import sys
input = sys.stdin.readline

for i in range(int(input())):                   # test case
    n = int(input())
    zeros=[1,0,1]                               # 2 까지 0 반환 수 DP테이블
    ones=[0,1,1]                                # 2 까지 1 반환 수 DP테이블
    if n >= 3:                                  # 3이상이면
        for i in range(2, n):                   # 바텀업
            zeros.append(zeros[i-1] + zeros[i]) # 현재 값에 이전 값 더한 것이이 다음 값
            ones.append(ones[i-1] + ones[i])
    print(zeros[n], ones[n])