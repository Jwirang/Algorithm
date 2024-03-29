import sys

ws = list(sys.stdin.readline().rstrip().split('-'))
b = 0
init = sum(map(int, ws[0].split('+')))
for w in ws[1:]:
    b += sum(map(int, w.split('+')))

print(init - b)