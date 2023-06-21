a = input()
b = input()

a = list(a)
b = list(b)

def to_string(list):
    res = ''
    for i in range(len(list) - 1, -1, -1):
        res += list[i]
    return res


result = []
for i in range(len(b) - 1, -1, -1):
    res = []
    carry = 0
    for j in range(len(a) - 1, -1, -1):
        b[i] = int(b[i])
        a[j] = int(a[j])

        # print(f'{b[i]} * {a[j]} = {b[i] * a[j]}')
        # if b[i] * a[j] + carry < 10:
        #     res.append(str(b[i] * a[j] + carry))
        # else:
        temp = b[i] * a[j] + carry
        carry = temp // 10
        res.append(str(temp % 10))
    if carry > 0:
        res.append(str(carry))

    sub = to_string(res)
    print(int(sub))
    result.append(sub)

final = 0
for i in range(len(result)):
    result[i] = result[i] + '0' * i
    final += int(result[i])
print(final)