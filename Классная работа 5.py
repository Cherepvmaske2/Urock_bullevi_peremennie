val_a = input()
flag = 0
count = 0
answer = 0
while val_a != 'СТОП':
    count += 1
    if 'Кот' in val_a or 'кот' in val_a:
        answer = count
        flag = 1
        break
    val_a = input()
if flag:
    print(answer)
else:
    print(-1)
