import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.q = [0]

    def insert(self, x):
        # 가장 마지막 노드에 추가
        self.q.append(x)
        # 추가한 노드의 인덱스
        index = len(self.q) - 1
        while index > 1:
            if self.q[index] < self.q[index // 2]:
                # 부모가 더 크면 스왑함
                self.q[index], self.q[index // 2] = self.q[index // 2], self.q[index]
                index = index // 2
            else:
                break

    def pop(self):
        # 힙이 비었을 경우 0출력
        if len(self.q) == 1:
            return 0
        # 제일 처음이랑 마지막이랑 스왑함
        self.q[1], self.q[-1] = self.q[-1], self.q[1]
        min = self.q.pop()
        self.sort()
        return min

    def sort(self):
        index = 1
        while len(self.q) > 1:
            _idx2 = index * 2
            _idx2p1 = index * 2 + 1
            next = index
            #해당 인덱스의 자식노드가 힙 내에 있고 자식이 현재 노드 보다 작다면
            if _idx2 < len(self.q) and self.q[_idx2] < self.q[next]:
                # 자식을 넥스트로 지정
                next = _idx2
            #해당 인덱스의 자식노드가 힙 내에 있고 자식이 현재 형제노드 보다 더 작다면
            if _idx2p1 < len(self.q) and self.q[_idx2p1] < self.q[next]:
                # 자식을 넥스트로 지정
                next = _idx2p1
            # next가 변경되었다면 위치 스왑후 인덱스 지정
            if next != index:
                self.q[index], self.q[next] = self.q[next], self.q[index]
                index = next
            else:
                break

if __name__ == "__main__":
    minHeap = MinHeap()
    for i in range(int(input())):
        x = int(input())
        if x == 0 :
            print(minHeap.pop())
        else:
            minHeap.insert(x)