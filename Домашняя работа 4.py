val_a = int(input())
val_b = input()
hobot = 0
hvost = 0
noga = 0
uho = 0
glaz = 0
rot = 0
slon = 0
while val_b != 'ОБЕД':
    if val_b == 'хобот':
        hobot += val_a
    elif val_b == 'хвост':
        hvost += val_a
    elif val_b == 'нога':
        noga += val_a
    elif val_b == 'ухо':
        uho += val_a
    elif val_b == 'глаз':
        glaz += val_a
    elif val_b == 'рот':
        rot += val_a
    val_a = int(input())
    val_b = input()
while (hobot >= 1) and (hvost >= 1) and (noga >= 4) and (uho >= 2) and (glaz >= 2) and (rot >= 1):
    hobot -= 1
    hvost -= 1
    noga -= 4
    uho -= 2
    glaz -= 2
    rot -= 1
    slon += 1
if slon:
    print('Есть слон!')
    print(slon)
else:
    print('Какие-то слоны нецелые. Пошли обедать.')
