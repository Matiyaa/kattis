for i in range(int(input())):
    input_ = input()
    if '=' in input_:
        print('skipped')
    else:
        a, b = map(int, input_.split('+'))
        print(a + b)
