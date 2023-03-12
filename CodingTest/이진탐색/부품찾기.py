import sys
input = sys.stdin.readline

def bSearch(arr, t, s, e):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            e = mid - 1
        elif arr[mid] < t:
            s = mid + 1

n = int(input())
parts = sorted(list(map(int, input().split())))
m = int(input())
fparts = list(map(int, input().split()))

for t in fparts:
    result = bSearch(parts, t, 0, n - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')