database = []
database_index = []
while True:
    n = input()
    if n == '-1':
        break
    else:
        penalty = 0
        time, task, answer = n.split()
        if answer == 'wrong':
            penalty = 1
        if task not in database_index:
            database_index.append(task)
            database.append([task, int(time), answer, penalty])
        else:
            index_ = database_index.index(task)
            penalty += database[index_][3]
            database[index_] = [task, int(time), answer, penalty]
total = 0
solved = 0
for i in database:
    if i[2] == 'right':
        total += i[1] + i[3] * 20
        solved += 1
print(solved, total)
