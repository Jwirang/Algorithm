import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

result = ""
for item in data:
    count, mystr = map(str, item.split())
    for i in mystr:
        result += i * int(count)
    result += '\n'

print(result)