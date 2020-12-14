number = int(input())
count_number = 0
count = 0
while number != count_number:
    val_1 = input()
    if val_1 != 'раз':
        count_number += 1
        print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
        count = 0
        continue
    else:
        count += 1
    val_2 = input()
    if val_2 != 'два':
        count_number += 1
        print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
        count = 0
        continue
    else:
        count += 1
    val_3 = input()
    if val_3 != 'три':
        count_number += 1
        print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
        count = 0
        continue
    else:
        count += 1
    val_4 = input()
    if val_4 != 'четыре':
        count_number += 1
        print(f'Правильных отсчётов было {count}, но теперь вы ошиблись.')
        count = 0
        continue
    else:
        count += 1
print('На сегодня хватит.')
