t = int(input())
rs = []
for i in range(t):
    a, b = input().split()
    rs.append(int(a) + int(b))
for j in range(t):
    print(rs[j])