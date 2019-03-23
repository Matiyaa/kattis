r, n = map(int, input().split())
free_rooms = list(range(1, r + 1))

for i in range(n):
    free_rooms.remove(int(input()))

if r == n:
    print('too late')
else:
    print(free_rooms[0])
