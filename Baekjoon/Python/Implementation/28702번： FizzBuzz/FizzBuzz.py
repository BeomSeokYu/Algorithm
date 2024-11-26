#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28702                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ro1864 <boj.kr/u/ro1864>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28702                          #+#        #+#      #+#     #
#    Solved: 2024/11/26 11:19:58 by ro1864        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
3의 배수 Fizz
5의 배수 Buzz
3과 5의 배수 FizzBuzz
그 외는 해당 숫자 그대로

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
...

숫자가 1개라도 있음 -> 다음 수 예측 가능

=> 연속된 3개의 수에서 숫자가 포함되지 않는 경우가 있는가?
3의 배수, 5의 배수, 3의 배수 -> 불가
5의 배수, 3의 배수, 5의 배수 -> 불가
즉, 없음
'''

import sys
input = sys.stdin.readline

li = []
for _ in range(3):
  li.append(input().rstrip())

idx = -1
val = -1
for i in range(len(li)):
  try:
    temp = int(li[i])
    idx = i
    val = temp
    break
  except ValueError:
    continue

val += 3 - idx

result = str(val)
if val % 3 == 0 and val % 5 == 0:
  result = 'FizzBuzz'
elif val % 3 == 0:
  result = 'Fizz'
elif val % 5 == 0:
  result = 'Buzz'

print(result)