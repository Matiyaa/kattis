input_ = input()
days = 0
index = 1
for i in input_:
    if index % 3 == 1 and i != 'P':
        days += 1
    elif index % 3 == 2 and i != 'E':
        days += 1
    elif index % 3 == 0 and i != 'R':
        days += 1
    index += 1
print(days)
