val_a = input()
flag = 0
count = 0
answer = 0
while val_a != 'СТОП':
    count += 1
    if 'Кот' in val_a or 'кот' in val_a:
        if answer == 0:
            answer = count
        flag = 1
    val_a = input()
if flag:
    print(answer)
else:
    print(-1)
