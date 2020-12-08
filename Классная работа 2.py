val_a = int(input())
flag = 0
for i in range(val_a):
    val_b = input()
    if 'Кот' in val_b or 'кот' in val_b:
        flag = 1
if flag:
    print('МЯУ')
else:
    print('НЕТ')
