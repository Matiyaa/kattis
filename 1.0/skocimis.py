x1, x2, x3 = map(int, input().split())
jumps = 0
while True:
    if x2 - x1 <= x3 - x2:
        if x1 < x2 and x2 + 1 != x3:
            x1 = x2
            x2 += 1
            jumps += 1
        else:
            break
    else:
        if x3 > x2 and x2 - 1 != x1:
            x3 = x2
            x2 -= 1
            jumps += 1
        else:
            break
print(jumps)
