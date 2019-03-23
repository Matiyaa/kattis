current_player = int(input()) - 1
timer = 210
bomb = 0
for i in range(int(input())):
    time, answer = input().split()
    if timer > 0:
        timer -= int(time)
        if timer < 0:
            bomb = current_player + 1
    if answer == 'T':
        current_player = (current_player + 1) % 8
print(bomb)
