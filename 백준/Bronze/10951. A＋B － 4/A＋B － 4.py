import sys
rs = []
while True:
    try:
        a, b = sys.stdin.readline().split()
        rs.append(int(a) + int(b))
    except:
        for i in range(len(rs)):
            print(rs[i])
        break