d1, d2 = map(int, input().split())
a = 0
options = []
for i in range(1, d1+1):
    for j in range(1, d2+1):
        a = i + j
        options.append(a)
mode_ = []
for i in set(options):
    mode_.append([options.count(i), i])
b = max(mode_)[0]
true_mode = []
for i in mode_:
    if i[0] == b:
        true_mode.append(i[1])
    else:
        pass
for i in true_mode:
    print(i)
