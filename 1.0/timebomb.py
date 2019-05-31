def liner(line_):
    return [line_[i:i + 3] for i in range(0, len(line_), 4)]


def fuse(code_, line_, length):
    return [code_[i] + line_[i] for i in range(length)]


legit = ['**** ** ** ****', '  *  *  *  *  *', '***  *****  ***', '***  ****  ****', '* ** ****  *  *',
         '****  ***  ****', '****  **** ****', '***  *  *  *  *', '**** ***** ****', '**** ****  ****']
first = str(input())
n = int(((len(first) - 3) / 4) + 1)
code = liner(first)
for i in range(4):
    line = liner(str(input()))
    code = fuse(code, line, n)

kaboom = False
true_code = ''
for i in code:
    if i in legit:
        true_code += str(legit.index(i))
    else:
        kaboom = True

if int(true_code) % 6 != 0:
    kaboom = True
else:
    pass

if kaboom:
    print('BOOM!!')
else:
    print('BEER!!')
