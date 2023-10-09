import sys
input = sys.stdin.readline

dict = {
    '.' : 0,
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26
}

def preorder(G, s):
    if s == '.':
        return
    print(s, end='')
    preorder(G, G[dict[s]][0])
    preorder(G, G[dict[s]][1])

def inorder(G, s):
    if s == '.':
        return
    inorder(G, G[dict[s]][0])
    print(s, end='')
    inorder(G, G[dict[s]][1])


def postorder(G, s):
    if s == '.':
        return
    postorder(G, G[dict[s]][0])
    postorder(G, G[dict[s]][1])
    print(s, end='')

N = int(input())
G = [[] for i in range(N + 1)]

for i in range(N):
    a, b, c = map(str, input().split())
    G[dict[a]].append(b)
    G[dict[a]].append(c)

preorder(G, 'A')
print()
inorder(G, 'A')
print()
postorder(G, 'A')
print()