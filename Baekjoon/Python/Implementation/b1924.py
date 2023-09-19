import sys
input = sys.stdin.readline

dow = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
nod = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
days = sum(nod[:(x - 1)]) + y
print(dow[(days%7)])