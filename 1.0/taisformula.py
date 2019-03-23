total = 0
tp = 0
vp = 0
for i in range(int(input())):
    ti, vi = map(float, input().split())
    if tp == 0 and vp == 0:
        tp = ti
        vp = vi
    else:
        total += (vp + vi) / 2 * (ti - tp)
        tp = ti
        vp = vi
print(total / 1000)
