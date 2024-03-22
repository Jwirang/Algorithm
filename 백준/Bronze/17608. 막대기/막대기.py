import sys
n = int(sys.stdin.readline())
stick_list = [int(sys.stdin.readline()) for i in range(n)]

stick_list.reverse()
stick = []
for i in stick_list:
    if len(stick) == 0:
        stick.append(i)
    elif stick[-1] < i:
        stick.append(i)

print(len(stick))