import sys
input = sys.stdin.readline

n = int(input())
pattern = ['**', '*'] # 1일 때 패턴
for i in range(n-1):
    for j in range(len(pattern)):
        pattern.append(pattern[j])              # 같은 패턴을 밑으로 추가
        pattern[j] += (' ' * j) + pattern[j]    # 같은 패턴을 공백을 1씩 추가하면 옆으로 추가
print('*') if n == 0 else print(*pattern, sep='\n')

# *pattern (Asterisk '*') : (리스트 압축 해제) 대괄호 콤마 없이 리스트를 하나하나 간격을 두고 출력
# sep='\n' : 요소 간격 사이에 \n 추가