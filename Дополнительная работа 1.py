val_a = int(input())
flag = 0
for i in range(val_a):
    val_b = input()
    if 'Кот' in val_b or 'кот' in val_b:
        flag = 1
    if 'Пёс' in val_b or 'пёс' in val_b:
        flag = 0
if flag:
    print('МЯУ')
else:
    print('НЕТ')
