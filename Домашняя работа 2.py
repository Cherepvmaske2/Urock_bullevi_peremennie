val_a = int(input())
evrasia = 1
ostasia = 0
for i in range(val_a):
    action = input()
    if action == 'С кем война?':
        if evrasia > ostasia:
            print('Евразия')
        else:
            print('Остазия')
    elif action == 'С кем мир?':
        if evrasia > ostasia:
            print('Остазия')
        else:
            print('Евразия')
    elif action == 'Меняем':
        if evrasia > ostasia:
            evrasia, ostasia = ostasia, evrasia
        else:
            ostasia, evrasia = evrasia, ostasia
