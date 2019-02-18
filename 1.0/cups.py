n = int(input())
cups = []
for i in range(n):
    a, b = map(str, input().split())
    radius = 0
    colour = ''
    try:
        int(a)
    except ValueError:
        colour = a
        radius = int(b)
    else:
        colour = b
        radius = int(int(a) / 2)
    cups.append((radius, colour))
cups.sort()
for i in cups:
    print(i[1])
