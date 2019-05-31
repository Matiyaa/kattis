a, b = map(int, input().split())
matrix = []
checked = set()
amoebas = 0
for _ in range(a):
    matrix.append(input())
for i in range(a):
    for j in range(b):
        if (i, j) not in checked and matrix[i][j] == '#':
            amoebas += 1
            need_check = [(i, j)]
            while need_check:
                checking = need_check.pop()
                x, y = checking[0], checking[1]
                if 0 <= x <= a - 1 and 0 <= y <= b - 1:
                    if (x, y) not in checked and matrix[x][y] == '#':
                        checked.add(checking)
                        need_check += [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
                        need_check += [(x, y - 1), (x, y + 1)]
                        need_check += [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
print(amoebas)
