import sys
input = sys.stdin.readline

str = input().rstrip()
for i in range(0, len(str)):
    if i != 0 and i % 10 == 0:
        print('')
    print(str[i], end='')