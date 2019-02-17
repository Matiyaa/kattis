G, S, C = map(int, input().split())
power = 3*G + 2*S + C
victory = [(8, 'Province'), (5, 'Duchy'), (2, 'Estate')]
treasure = [(6, 'Gold'), (3, 'Silver'), (0, 'Copper')]
bvictory = ''
btreasure = ''
for item in victory:
    if power >= item[0]:
        bvictory = item[1]
        break
for item in treasure:
    if power >= item[0]:
        btreasure = item[1]
        break
if bvictory == '':
    print(btreasure)
else:
    print(bvictory, 'or', btreasure)
