def slot(char):
    if char == '.':
        return 0
    elif char == 'X':
        return 1
    else:
        return 5


R, C = map(int, input().split())
lines = []
output = ''
for i in range(R):
    lines.append(input())
for j in range(R-1):
    for _ in range(C - 1):
        cars = slot(lines[j][_])
        cars += slot(lines[j][_+1])
        cars += slot(lines[j+1][_])
        cars += slot(lines[j+1][_+1])
        if cars <= 4:
            output += str(cars)
for k in range(5):
    print(output.count(str(k)))
