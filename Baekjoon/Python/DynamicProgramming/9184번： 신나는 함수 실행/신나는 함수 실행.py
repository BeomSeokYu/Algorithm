#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9184                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9184                           #+#        #+#      #+#     #
#    Solved: 2024/05/24 15:42:28 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

d = dict() # 하향식 재귀의 메모이제이션을 위한 딕셔너리

def w(a, b, c):
    key = str(a) + str(b) + str(c)
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if d.get(key) != None:
        return d.get(key)
    if a < b and b < c:
        res = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        d[key] = res
        return res
    res = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    d[key] = res
    return res

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')