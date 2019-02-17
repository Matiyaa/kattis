word = input()
a = len(word)
i = 1
hiss = 0
while i < a:
    if word[i - 1] + word[i] == 'ss':
        hiss = 1
        break
    else:
        i += 1
if hiss == 0:
    print('no hiss')
else:
    print('hiss')
