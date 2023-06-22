import sys

t = int(input())
rs = []
for i in range(t):
    a, b = sys.stdin.readline().split()
    idx = 0
    rs.append(int(a) + int(b))
for i in range(len(rs)):
    print(rs[i])