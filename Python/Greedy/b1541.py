import sys
input = sys.stdin.readline

result = 0

s = input().strip()
idx = s.find('-')
if idx == -1:
    for num in s.split('+'):
        result += int(num)
else:
    for num in s[:idx].split('+'):
        result += int(num)
    for num in s[idx+1:].replace('+', '-').split('-'):
        result -= int(num)
print(result)

'''
'-' 뒤의 '+' 는 괄호로 묶여 -가 된다.
최초 '-' 뒤에는 모무 '-'가 된다.

1 + 2 - 3 - (4 + 5) - 6 - (7 + 8 + 9) - 10 - 11 - 12
1 + 2 + 3 + 4
1 + 2 - (3 + 4)
1 + 2 + 3 - 4
'''
