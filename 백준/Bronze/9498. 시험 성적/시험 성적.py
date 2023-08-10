# 시험성적
n = int(input())
grade = n // 10
if grade >= 9:
    print('A')
elif grade == 8:
    print('B')
elif grade == 7:
    print('C')
elif grade == 6:
    print('D')
else:
    print('F')