import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    s = input()
    cmd = s[:2]
    if cmd == 'pu':
        stack.append(int(s[5:]))
    elif cmd == 'po':
        print(stack.pop()) if len(stack) > 0 else print(-1)
    elif cmd == 'si':
        print(len(stack))
    elif cmd == 'em':
        print(0) if len(stack) > 0 else print(1)
    elif cmd == 'to':
        print(stack[len(stack)-1]) if len(stack) > 0 else print(-1)