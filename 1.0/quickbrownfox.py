from string import ascii_lowercase

for i in range(int(input())):
    phrase = input()
    missing = ascii_lowercase
    for i in phrase:
        letter = i.lower()
        if letter in missing:
            missing = missing.replace(letter, '')
        if missing == '':
            print('pangram')
            break
    if missing != '':
        print(f'missing {missing}')
