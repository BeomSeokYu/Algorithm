import sys

input = sys.stdin.readline

stack = []
N = int(input())
for _ in range(N):
    inst = list(map(int, input().split()))
    if inst[0] == 1:
        stack.append(inst[1])
    elif inst[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif inst[0] == 3:
        print(len(stack))
    elif inst[0] == 4:
        print(1) if not stack else print(0)
    elif inst[0] == 5:
        print(stack[-1]) if stack else print(-1)