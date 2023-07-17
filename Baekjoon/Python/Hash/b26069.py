import sys
input = sys.stdin.readline

meet = set()
meet.add('ChongChong')
result = 0
N = int(input())
for _ in range(N):
    a, b = input().split()
    if a in meet and b not in meet:
        meet.add(b)
    elif a not in meet and b in meet:
        meet.add(a)
if len(meet) == 1:
    meet.pop()
print(len(meet))