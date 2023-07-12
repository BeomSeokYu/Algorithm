import sys
input = sys.stdin.readline

a = []
_sum = 0
for _ in range(3):
    a.append(int(input()))
a.sort()
_sum = sum(a)
if _sum != 180:
    print('Error')
elif a[0] == a[-1]:
    print('Equilateral')
elif a[0] == a[1] or a[1] == a[2]:
    print('Isosceles')
else:
    print('Scalene')