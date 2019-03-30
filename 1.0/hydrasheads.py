def game(heads, tails):
    moves = 0
    while True:
        if heads % 2 == 1 and tails == 0:
            return -1
        elif heads == 0 and tails == 0:
            return moves
        if heads % 2 == 0 and heads > 0:
            heads -= 2
            moves += 1
        elif tails % 2 == 0 and heads != 0:
            tails -= 2
            heads += 1
            moves += 1
        elif tails % 4 == 0:
            tails -= 2
            heads += 1
            moves += 1
        else:
            tails += 1
            moves += 1


while True:
    H, T = map(int, input().split())
    if H == 0 and T == 0:
        break
    print(game(H, T))
