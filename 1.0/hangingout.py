L, x = map(int, input().split())
people_inside = 0
groups_denied = 0
for i in range(x):
    event, people = input().split()
    people = int(people)
    if event == 'enter':
        if people_inside + people > L:
            groups_denied += 1
        else:
            people_inside += people
    else:
        people_inside -= people
print(groups_denied)
