val_a = int(input())
count = 0
result = 0
while val_a != 0:
    if result != 10:
        result += val_a
        count += 1
    if result == 10:
        break
    val_a = int(input())
print(count)
