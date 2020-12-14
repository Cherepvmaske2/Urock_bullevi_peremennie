val_a = input()
first = 0
answer = 0
count = 0
while val_a != 'СТОП':
    count += 1
    if 'кот' in val_a or 'Кот' in val_a:
        if first == 0:
            first = count
        answer += 1
    val_a = input()
print(answer, end=' ')
if first:
    print(first)
else:
    print(-1)
