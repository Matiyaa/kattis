n = int(input())
for i in range(n):
    a = input()
    b = input()
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += '.'
        else:
            c += '*'
    print(a)
    print(b)
    print(c)
    print()
