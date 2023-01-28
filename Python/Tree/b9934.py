import sys
input = sys.stdin.readline

def bfsTree(tree, i):
    root = len(tree)//2
    if i == 0:
        l.append(tree[root])
        return
    bfsTree(tree[:root], i-1)
    bfsTree(tree[root+1:], i-1)

l= []
k = int(input())
cbTree = list(map(int, input().split()))
for i in range(k):
    bfsTree(cbTree, i)
    for _ in range(len(l)):
        print(l.pop(0), end=" ")
    print()