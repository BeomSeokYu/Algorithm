import sys
input = sys.stdin.readline

_map = {}
for _ in range(int(input())):
    name, log = input().split()
    _map[name] = log

for name in sorted(_map.keys(), reverse=True):
    if _map[name] == 'enter':
        print(name)