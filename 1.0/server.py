n, T = map(int, input().split())
task = input().split()
completed = 0
for i in task:
    T -= int(i)
    if T >= 0:
        completed += 1
    else:
        break
print(completed)
