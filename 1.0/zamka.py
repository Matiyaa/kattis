L = int(input())
D = int(input())
x = int(input())
N = 0
M = 0

for i in range(L, D + 1):
    j = str(i)
    sum_ = 0
    for number in j:
        sum_ += int(number)
    if sum_ == x:
        N = i
        print(N)
        break

for i in range(D, L - 1, -1):
    j = str(i)
    sum_ = 0
    for number in j:
        sum_ += int(number)
    if sum_ == x:
        M = i
        print(M)
        break
