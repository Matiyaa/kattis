while True:
    N = input()
    N_sum = 0
    for i in N:
        N_sum += int(i)
    N = int(N)
    if N == 0:
        break
    else:
        for p in range(11, 1000):
            x = N * p
            y = str(x)
            y_sum = 0
            for i in y:
                y_sum += int(i)
            if y_sum == N_sum:
                break
    print(p)
