import sys

t = int(input())
rs = []
for i in range(t):
    a, b = sys.stdin.readline().split()
    idx = 0
    rs.append([int(a), int(b), int(a) + int(b)])
for i in range(len(rs)):
    print(f'Case #{i + 1}: {rs[i][0]} + {rs[i][1]} = {rs[i][2]}')