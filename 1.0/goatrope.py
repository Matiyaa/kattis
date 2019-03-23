x, y, x1, y1, x2, y2 = map(int, input().split())
home_x = [x1, x2, x2, x1]
home_y = [y1, y1, y2, y2]
distances = []
if y1 <= y <= y2:
    distances.append(min(abs(x - x1), abs(x - x2)))
if x1 <= x <= x2:
    distances.append(min(abs(y - y1), abs(y - y2)))
for i in range(4):
    distance = ((x - home_x[i]) ** 2 + (y - home_y[i]) ** 2) ** 0.5
    distances.append(distance)
print(min(distances))
