import sys
rs = []
while True:
    a, b = sys.stdin.readline().split()
    if a == '0' and b == '0':
        for i in range(len(rs)):
            print(rs[i])
        break
    rs.append(int(a) + int(b))