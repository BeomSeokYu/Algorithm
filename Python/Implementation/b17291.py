import sys
input = sys.stdin.readline

n = int(input())

# 벌래 수명 깍고 수명 다했으면 죽이는 함수
def minusLife(bug):
    didx = []
    for i in range(len(bug)):
        bug[i] -= 1
        if bug[i] == 0:
            didx.append(i-len(didx))    # 이놈 죽어야됨 (remove 고려해 길이만끔 뺏음)
    for i in didx:
        bug.remove(i)                   # 죽임 ㅅㄱ
    return bug

bug = [3]                               # 처음엔 홀수라 3 넣어줌
for i in range(2, n+1):                 # n년까지 반복 (n <=20)
    #print(bug)
    for j in range(len(bug)):
        bug.append(5) if i % 2 == 0 else bug.append(4) # 바로 마이너스라 5랑 4임
    bug = minusLife(bug)                               # 뒤질놈은 뒤지고 수명 깍음
print(len(bug))                                        # 살아 남은 놈 출력

# 이거 시간초과나면 힙쓸려 했는데 통과됐네??