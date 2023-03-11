import sys
input = sys.stdin.readline

ScoreDic = {
    'A+':   4.5,
    'A0':	4.0,
    'B+':	3.5,
    'B0':	3.0,
    'C+':	2.5,
    'C0':	2.0,
    'D+':	1.5,
    'D0':	1.0,
    'F':	0.0
}
sumScore = 0
mulScoSub = 0
for i in range(20):
    n, s, g = input().split()
    s = float(s)
    if g != 'P':
        sumScore += s
        mulScoSub += ScoreDic[g] * s
print('%.6f'%(mulScoSub/sumScore))


