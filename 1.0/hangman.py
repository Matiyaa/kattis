word = input()
letters = input()
fails = 0
for i in letters:
    if i in word:
        word = word.replace(i, '')
    else:
        fails += 1
    if word == '':
        break
if fails >= 10:
    print('LOSE')
else:
    print('WIN')
