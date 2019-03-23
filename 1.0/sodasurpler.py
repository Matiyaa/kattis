e, f, c = map(int, input().split())
money = e + f
drink = 0
while money >= c:
    bought = money // c
    money -= (bought * c) - bought
    drink += bought
print(drink)
