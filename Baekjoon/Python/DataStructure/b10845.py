import sys
input = sys.stdin.readline

queue = []
for i in range(int(input())):
    s = input()
    cmd = s[:2]
    if cmd == 'pu':
        queue.append(int(s[5:]))
    elif cmd == 'po':
        print(queue.pop(0)) if len(queue) > 0 else print(-1)
    elif cmd == 'si':
        print(len(queue))
    elif cmd == 'em':
        print(0) if len(queue) > 0 else print(1)
    elif cmd == 'fr':
        print(queue[0]) if len(queue) > 0 else print(-1)
    elif cmd == 'ba':
        print(queue[len(queue)-1]) if len(queue) > 0 else print(-1)