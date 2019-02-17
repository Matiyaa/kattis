names = input().split('-')
n = len(names)
autori = ""
for i in range(n):
    autori += names[i][0]
print(autori)
