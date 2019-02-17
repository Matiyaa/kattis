N = int(input())
X = 0
for i in range(N):
    a = input()
    X += int(a[:-1])**int(a[-1])
print(X)
