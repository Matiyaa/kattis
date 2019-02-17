pset = list(map(int, input().split()))
cset = [1, 1, 2, 2, 2, 8]
oset = []
i = 0
while i < 6:
    x = cset[i] - pset[i]
    oset.append (x)
    i += 1
osett = ' '.join(str(e) for e in oset)
print(osett)
