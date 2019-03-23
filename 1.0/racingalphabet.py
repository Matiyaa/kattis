from math import pi

circle = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
tile = pi * 60 / 28
for i in range(int(input())):
    aphorism = input()
    time = len(aphorism)
    for j in range(len(aphorism) - 1):
        start = circle.index(aphorism[j])
        finish = circle.index(aphorism[j + 1])
        option1 = (start - finish) % 28
        option2 = (finish - start) % 28
        time += min(option1, option2) * tile / 15
    print(time)
