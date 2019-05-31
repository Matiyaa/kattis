def where_ball_is(ball, move):
    if move == 'A':
        if ball == 1:
            return 2
        elif ball == 2:
            return 1
        else:
            return ball
    elif move == 'B':
        if ball == 2:
            return 3
        elif ball == 3:
            return 2
        else:
            return ball
    else:
        if ball == 1:
            return 3
        elif ball == 3:
            return 1
        else:
            return ball


ball = 1
moves = input()
for i in moves:
    ball = where_ball_is(ball, i)
print(ball)
