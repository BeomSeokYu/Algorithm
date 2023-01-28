import sys
input = sys.stdin.readline

times = []
result = 0
for i in range(int(input())):
    times.append(tuple(map(int, input().split())))
times = sorted(sorted(times, key=lambda x:x[0]), key=lambda x:x[1])
temp = ()
for i in range(0, len(times)):
    if(i == 0) :
        temp = times[0]
        result += 1
        continue
    if times[i][0] == times[i][1] or times[i][0] >= temp[1] :
        temp = times[i]
        result += 1
print(result)