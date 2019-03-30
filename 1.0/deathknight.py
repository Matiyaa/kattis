lost = 0
tries = int(input())
for i in range(tries):
    spells = input()
    for j in range(len(spells)):
        if spells[j] == 'C' and j < len(spells) - 1:
            if spells[j + 1] == 'D':
                lost += 1
                break
print(tries - lost)
