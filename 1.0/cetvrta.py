r1 = []
r2 = []
for i in range(3):
    r1_, r2_ = map(int, input().split())
    r1.append(r1_)
    r2.append(r2_)
for i in r1:
    for a in r2:
        if r1.count(i) == 1 and r2.count(a) == 1:
            print(str(i)+" "+str(a))
