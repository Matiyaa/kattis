n = 1
while True:
    test = input()
    output = []
    pointer = 0
    if test == '0':
        break
    else:
        for i in range(int(test)):
            a = input()
            if i % 2 == 1:
                pointer += 1
                output.insert(pointer, a)
            else:
                output.insert(pointer, a)
    print(f'SET {n}')
    n += 1
    for i in output:
        print(i)
