import sys
input = sys.stdin.readline

n = int(input())
nSet = set(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

for i in mList:
    print(1) if i in nSet else print(0)

# Set은 중복이 없는 원소들이므로 탐색시간이 리스트에 비해 굉장히 짧다