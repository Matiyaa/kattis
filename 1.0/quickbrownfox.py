from string import ascii_lowercase

for i in range(int(input())):
    phrase = input()
    missing = ascii_lowercase
    for j in phrase:
        letter = j.lower()
        if letter in missing:
            missing = missing.replace(letter, '')
        if missing == '':
            print('pangram')
            break
    if missing != '':
        print(f'missing {missing}')
