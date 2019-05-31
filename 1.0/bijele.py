p_set = list(map(int, input().split()))
c_set = [1, 1, 2, 2, 2, 8]
o_set = []
i = 0
while i < 6:
    x = c_set[i] - p_set[i]
    o_set.append(x)
    i += 1
new_o_set = ' '.join(str(e) for e in o_set)
print(new_o_set)
