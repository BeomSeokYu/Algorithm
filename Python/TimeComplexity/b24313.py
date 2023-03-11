a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = set()
for i in range(n0, 101):
    fn = a1*i + a0
    gn = i

    if fn <= c*gn:
        result.add(1)
    else:
        result.add(0)

if 0 in result:
    print(0)
else:
    print(1)