X = int(input())
N = int(input())
to_use = X * (N + 1)
for i in range(N):
    to_use -= int(input())
print(to_use)
