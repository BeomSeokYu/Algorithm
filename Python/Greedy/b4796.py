import sys
input = sys.stdin.readline

case = 1
while True:
    result = 0
    l, p, v = map(int, input().split())
    if (l, p, v) == (0, 0, 0):
        break
    result += (v // p) * l
    if v % p >= l:
        result += l
    else:
        result += v % p
    print(f"Case {case}: {result}")
    case += 1
