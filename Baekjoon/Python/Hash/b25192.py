import sys
input = sys.stdin.readline

N = int(input())
hash = {}
isEntered = False
result = 0
for i in range(N):
    str = input().rstrip()
    if str == 'ENTER':
        hash.clear()
        isEntered = True
        continue
    try:
        if isEntered:
            hash[str]
    except KeyError:
        hash[str] = str
        result += 1
print(result)
