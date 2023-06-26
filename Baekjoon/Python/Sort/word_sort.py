import sys
l = list()
for i in range(int(input())):
    temp = (sys.stdin.readline()).strip()
    l.append((temp, len(temp)))
for i in sorted(sorted(list(set(l)), key=lambda x:x[0]), key=lambda x:x[1]):
    print(i[0])