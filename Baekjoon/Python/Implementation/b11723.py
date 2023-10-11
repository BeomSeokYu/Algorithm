import sys
input = sys.stdin.readline

M = int(input())
S = set()
el = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
for i in range(M):
    str_li = input().split()
    oper = ''
    x = 0
    if len(str_li) > 1:
        oper, x = str_li[0], int(str_li[1])
    else:
        oper = str_li[0]

    if oper == 'add':
        S.add(x)
    elif oper == 'remove':
        if x in S:
            S.remove(x)
    elif oper == 'check':
        print(1 if x in S else 0)
    elif oper == 'toggle':
        S.remove(x) if x in S else S.add(x)
    elif oper == 'all':
        S = el.copy()
    elif oper == 'empty':
        S.clear()