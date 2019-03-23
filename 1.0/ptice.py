def adrian(answer, index_):
    mod = index_ % 3
    if answer == 'A' and mod == 1:
        return 1
    elif answer == 'B' and mod == 2:
        return 1
    elif answer == 'C' and mod == 0:
        return 1
    else:
        return 0


def bruno(answer, index_):
    mod = index_ % 4
    if answer == 'A' and mod == 2:
        return 1
    elif answer == 'B' and (mod == 1 or mod == 3):
        return 1
    elif answer == 'C' and mod == 0:
        return 1
    else:
        return 0


def goran(answer, index_):
    mod = index_ % 6
    if answer == 'A' and (mod == 3 or mod == 4):
        return 1
    elif answer == 'B' and (mod == 5 or mod == 0):
        return 1
    elif answer == 'C' and (mod == 1 or mod == 2):
        return 1
    else:
        return 0


length = int(input())
sequence = input()
boys = ['Adrian', 'Bruno', 'Goran']
correct = [0, 0, 0]
index = 1
for i in sequence:
    correct[0] += adrian(i, index)
    correct[1] += bruno(i, index)
    correct[2] += goran(i, index)
    index += 1

best = max(correct)
print(best)
index = 0
for i in correct:
    if i == best:
        print(boys[index])
    index += 1
