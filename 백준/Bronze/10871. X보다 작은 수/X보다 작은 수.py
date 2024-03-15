import sys
a,b = map(int, sys.stdin.readline().split())
c = input().split()

result = [int(x) for x in c if int(x) < b]

output = " ".join(map(str, result))
print(output)