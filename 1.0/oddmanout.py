for i in range(int(input())):
    G = input()
    codes = input().split()
    for j in codes:
        if codes.count(j) == 1:
            print(f'Case #{i + 1}: {j}')
