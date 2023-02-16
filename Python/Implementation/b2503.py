import sys, itertools
input = sys.stdin.readline

all = list(itertools.permutations(range(1, 10), 3)) # 모든 경우의 수 다 확인할거임

for _ in range(int(input())):               # 질문 반복
    num, st, ba = map(int, input().split())
    num = list(map(int, str(num)))          # 숫자 한자리씩 리스트
    idx = 0                                 # pop 고려한 인덱스 조절용
    for i in range(len(all)):               # 모든 경우 돌면서
        i -= idx
        s = 0
        b = 0
        for j in range(3):
            if all[i][j] == num[j]:         # 같은 자리면
                s += 1                      # 스트라이크 카운트
            elif num[j] in all[i]:          # 다른 자리면
                b += 1                      # 볼 카운트
        if s != st or b != ba:              # 둘 중 하나라고 질문이랑 다르면
            all.pop(i)                      # 과감하게 빼버림
            idx += 1                        # 뺐으니 인덱스 조절

print(len(all))                             # 남은 놈은 답일 가능성 있는 놈들임