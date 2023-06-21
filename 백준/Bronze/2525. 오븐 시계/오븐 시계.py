h, m = input().split()
n = int(input())

h = int(h)
m = int(m)

f_m = (n + m) % 60
f_h = (n + m) // 60

if f_h >= 1:
    h += f_h
    if h >= 24:
        h -= 24
    print(h, f_m)
else:
    print(h, f_m)