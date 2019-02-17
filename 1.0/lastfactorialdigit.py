def factorial(x):
    factor = 1
    if x == 1:
        return 1
    else:
        while x > 1:
            factor = factor * x
            x -= 1
        return factor


T = int(input())
i = 0

while i < T:
    N = int(input())
    x = str(factorial(N))
    i += 1
    print(x[-1])
