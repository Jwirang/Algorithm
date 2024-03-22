import sys
t = int(sys.stdin.readline())
prnth_string = [sys.stdin.readline().split() for i in range(t)]

for i in prnth_string:
    prnth = [char for char in i[0]]
    res = []
    for j in prnth:
        if j == '(':
            res.append(j)
        elif j == ')':
            if len(res) == 0: 
                print('NO')
                break
            else:
                res.pop()         
    else:
        if len(res) == 0:
            print('YES')
        else:
            print('NO')
    