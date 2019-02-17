points = 0
hs = 0
index = 0
for i in range(5):
    points = sum(map(int, input().split()))
    if points > hs:
        hs = points
        index = i+1
print(index, hs)
