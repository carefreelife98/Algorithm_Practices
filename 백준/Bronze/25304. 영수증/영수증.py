# 영수증
x = int(input())
n = int(input())
sum = 0
for i in range(n):
    a, b = input().split()
    sum += int(a) * int(b)
if sum == x:
    print('Yes')
else:
    print('No')
