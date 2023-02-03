import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mainStack = [] # 메인 키입력 저장
    subStack = []  # 커서 이동 처리 임시 스택

    keyInput = input().rstrip()  # 키입력
    for key in keyInput:
        if key == '<':                          # 오른쪽 커서 이동의 경우
            if len(mainStack) > 0:              # 메인에 값이 있다면
                subStack.append(mainStack.pop())  # 서브스택으로 이동
        elif key == '>':                        # 왼쪽 커서 이동의 경우
            if len(subStack) > 0:               # 서브스택으로 이동된 값이 있다면
                mainStack.append(subStack.pop())  # 다시 메인으로 이동
        elif key == '-':                        # 백스페이스 입력의 경우
            if len(mainStack) > 0:              # 메인의 값이 있다면
                mainStack.pop()                 # 상단 값만 빼버림
        else:
            mainStack.append(key)         # 그외 입력은 메인에 삽입
    while len(subStack) > 0:              # 입력 반복 이후 서브스택에 값이 남아 있는 경우
        mainStack.append(subStack.pop())  # 메인으로 이동

    for i in mainStack:               # 메인 출력
        print(i, end='')
    print()