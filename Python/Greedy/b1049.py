import sys, math
input = sys.stdin.readline

# n: 끊어진 기타줄 갯수 0 < n <= 100
# m: 기타줄 브랜드 0 < m <= 50
n, m = map(int, input().split())
packPrices = []
onePrices = []
for i in range(m):
    # p: 패키지 가격 (6개) (<=1000)
    # o: 낱개 가격 (<=1000)
    p, o = map(int, input().split())
    packPrices.append(p)
    onePrices.append(o)
packPrices.sort()
onePrices.sort()
if packPrices[0] < onePrices[0]*6:
    a = n//6
    b = n%6
    if (b * onePrices[0] < packPrices[0]):
        print(a * packPrices[0] + b * onePrices[0])
    else:
        print((a + 1) * packPrices[0])
else:
    print(n * onePrices[0])