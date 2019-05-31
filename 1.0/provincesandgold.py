G, S, C = map(int, input().split())
power = 3*G + 2*S + C
victory = [(8, 'Province'), (5, 'Duchy'), (2, 'Estate')]
treasure = [(6, 'Gold'), (3, 'Silver'), (0, 'Copper')]
b_victory = ''
b_treasure = ''
for item in victory:
    if power >= item[0]:
        b_victory = item[1]
        break
for item in treasure:
    if power >= item[0]:
        b_treasure = item[1]
        break
if b_victory == '':
    print(b_treasure)
else:
    print(b_victory, 'or', b_treasure)
