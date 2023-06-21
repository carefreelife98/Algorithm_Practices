a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

temp = [a, b, c]

if a != b != c != a:
    temp.sort()
    print(temp[len(temp) - 1] * 100)
elif a == b == c:
    print(10000 + a * 1000)
else:
    for i in range(len(temp)):
        if temp.count(temp[i]) == 2:
            # print(temp[i])
            print(1000 + temp[i] * 100)
            break