N = int(input())
side = 2
for i in range(N):
    side += (side - 1)
print(side**2)
