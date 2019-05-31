n = int(input())
for i in range(n):
    a = input()
    b = input()
    c = ''
    for j in range(len(a)):
        if a[j] == b[j]:
            c += '.'
        else:
            c += '*'
    print(a)
    print(b)
    print(c)
    print()
