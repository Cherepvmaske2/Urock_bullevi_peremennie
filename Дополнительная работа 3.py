val = int(input())
val_1 = val + 1
answer_1 = 0
answer_2 = 0
while val != 0:
    if val > val_1:
        answer_1 = val
        break
    else:
        val_1 = val
        val = int(input())
while val != 0:
    if val < val_1:
        answer_2 = val
        break
    else:
        val_1 = val
        val = int(input())
while val != 0:
    val = int(input())
print(answer_1, answer_2, answer_2 - answer_1)
