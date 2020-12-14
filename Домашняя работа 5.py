number = int(input())
val_a = input()
count = 0
while val_a != 'КОНЕЦ':
    if 'доска' in val_a or 'дощечка' in val_a:
        count += 1
        print(f'Прибили {count} дощечку.', end='\n')
    if count == number:
        break
    val_a = input()
if count != number:
    print('МАЛОВАТО')
else:
    print('ГОТОВО')
