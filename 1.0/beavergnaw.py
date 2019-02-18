from math import pi


while True:
    D, V = map(int, input().split())
    if D == 0 and V == 0:
        break
    else:
        print((((D ** 3) * pi / 6 - V) / (pi / 6)) ** (1.0/3))
