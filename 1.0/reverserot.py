alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')
while True:
    encrypted = ''
    line = input()
    if line == '0':
        break
    shift, text = line.split()
    shift = int(shift)
    for i in text:
        index = (alphabet.index(i) + shift) % 27
        index -= (alphabet.index(i) + shift) // 27
        encrypted += alphabet[index]
    print(encrypted[::-1])
