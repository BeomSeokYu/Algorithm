import sys
input = sys.stdin.readline

n, c = map(int, input().split())

def paramSearch(arr, t, s, e):
    result = 0
    while s <= e:
        dl = []
        pre_d = 0
        mid = (s + e) // 2
        for i in arr:
            if i > t:
                pass

li = []
for i in range(n):
    li.append(int(input()))
li.sort()

d = []
for i in range(len(li)-1):
    d.append(li[i+1] - li[i])

print(d)