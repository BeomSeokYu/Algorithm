import sys
input = sys.stdin.readline

N = int(input())

topings = input().split()
cheese = set()
for toping in topings:
    if len(toping) > 5 and toping[-6:] == 'Cheese':
        cheese.add(toping)
print('yummy' if len(cheese) >= 4 else 'sad')