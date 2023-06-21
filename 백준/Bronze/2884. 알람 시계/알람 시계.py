h, m = input().split()
h = int(h)
m = int(m)

if h == 0:
    if m < 45:
        h = 23
        m = 60 - abs(m - 45)
    else:
        m -= 45
    print(h, m)
elif h > 0:
    if m < 45:
        h -= 1
        m = 60 - abs(m - 45)
    else:
        m -= 45
    print(h, m)
