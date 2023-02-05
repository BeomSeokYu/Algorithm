s = input()
result = 2 + len(s)
for i in s:
    if i == '_':
        result += 5
print(result)