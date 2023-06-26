import sys
input = sys.stdin.readline

# 스택 기능과 스택의 항목 수 반환 기능을 갖는 클래스
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def state(self):
        return len(self.stack)

for i in range(int(input())):
    psStack = Stack()           # 스택 객체 생성
    testData = input()          # 문자열 데이터 입력받음
    for data in testData:       # 문자열의 문자 반복
        if data == '(':         # 문자가 열린 괄호면 스택에 푸쉬
            psStack.push(data)
        elif data ==')':        # 문자가 닫힌 괄호면 스택에서 팝
            try:
                psStack.pop()
            except IndexError as e: # 빈 스택에서 팝 시도시 그 데이터를 푸쉬(invaild 처리를 위해)하고 반복 종료
                psStack.push(data)
                break
    print('YES') if psStack.state() == 0 else print('NO')   #스택이 비었으면 YES 아니면 NO