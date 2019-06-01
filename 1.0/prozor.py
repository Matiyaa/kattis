R, S, K = map(int, input().split())
picture = []
shot_options = {}

for i in range(R):
    picture.append(list(input()))

for y in range(1, R - 1):
    for x in range(1, S - 1):
        flies = 0
        starting_y = y
        starting_x = x
        if y + K - 1 > R or x + K - 1 > S:
            pass
        else:
            for i in range(K - 2):
                for j in range(K - 2):
                    if picture[y + i][x + j] == '*':
                        flies += 1
            if flies > 0:
                shot_options[flies] = [starting_y, starting_x]

best_case = max(sorted(shot_options))
starting_point = shot_options[best_case]
starting_point[0] = starting_point[0] - 1
starting_point[1] = starting_point[1] - 1
picture[starting_point[0]][starting_point[1]] = '+'
picture[starting_point[0]][starting_point[1] + K - 1] = '+'
picture[starting_point[0] + K - 1][starting_point[1]] = '+'
picture[starting_point[0] + K - 1][starting_point[1] + K - 1] = '+'

for i in range(1, K - 1):
    picture[starting_point[0]][starting_point[1] + i] = '-'
    picture[starting_point[0] + K - 1][starting_point[1] + i] = '-'
    picture[starting_point[0] + i][starting_point[1]] = '|'
    picture[starting_point[0] + i][starting_point[1] + K - 1] = '|'

print(best_case)
for i in picture:
    print(''.join(i))
