N = input()
temps = map(int, input().split())
zero = 0
for i in temps:
    if i < 0:
        zero += 1
    else:
        pass
print(zero)
