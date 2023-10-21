import sys
input = sys.stdin.readline

def explosion(main, exp):
    stack = []
    exp_len = len(exp)
    for i in range(len(main)):
        stack.append(main[i])
        if ''.join(stack[-exp_len:]) == exp:
            for _ in range(exp_len):
                stack.pop()
    return ''.join(stack)


def boom(main_str, exp_str):
    pre_len = len(main_str)
    main_str = explosion(main_str, exp_str);
    if len(main_str) == pre_len:
        return main_str
    else:
        return boom(main_str, exp_str)

main_str = input().rstrip()
exp_str = input().rstrip()

result = boom(main_str, exp_str)
print(result if result else 'FRULA')