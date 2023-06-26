import sys
input = sys.stdin.readline
'''
30의 배수를 판정하려면 10의 배수, 3의 배수인지를 확인하면 되는데, 

1. 일단 10의 배수 판별법은 끝자리가 0이면 됩니다. 30 x N의 형태는 반드시 0으로 끝나게 되므로, 각 자리수를 크기순으로 재배열한다고 해도, 반드시 끝자리는 0이 됩니다.

2. 3의 배수 판별법은 각 자리수의 합이 3의 배수이면 됩니다. 각 자리수의 합은 숫자를 재배열해도 그대로이므로 원래 수가 3의 배수였다면, 어떻게 재배열해도 3의 배수가 됩니다.
'''
n = list(map(int, input().rstrip()))
if 0 not in n:
    print(-1)
else:
    if sum(n) % 3 != 0:
        print(-1)
    else:
        n.sort(reverse=True)
        s = ''
        for i in n:
            s += str(i)
        print(int(s))