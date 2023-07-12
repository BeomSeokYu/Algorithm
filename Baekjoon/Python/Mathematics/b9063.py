import sys
input = sys.stdin.readline

dots = []
N = int(input())
for i in range(N):
    dots.append((tuple(map(int, input().split()))))
dots.sort(key=lambda x: x[0])
x_min = dots[0][0]
x_max = dots[-1][0]
dots.sort(key=lambda x: x[1])
y_min = dots[0][1]
y_max = dots[-1][1]
print((x_max-x_min) * (y_max - y_min))